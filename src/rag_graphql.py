import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--api_key', type=str, required=True, help='Your ISDM OpenAI API like Key')
parser.add_argument('--api_jwt', type=str, required=True, help='Your ISDM JWT')
parser.add_argument('--model', type=str, default="solidrust/Codestral-22B-v0.1-hf-AWQ")
args = parser.parse_args()

import logging
logging.basicConfig(
    filename='logs/pipeline.log',  # Name of the log file
    filemode='a',        # Append mode; use 'w' for overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
    level=logging.INFO   # Set the logging level
)

from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import requests
import urllib.parse

from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
import pandas as pd
import re
from transformers import AutoTokenizer, RobertaModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import socket
from datetime import datetime
hostname = socket.gethostname()
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
import Context_GraphQL
import faiss
import numpy as np
import time

if args.model == "solidrust/Codestral-22B-v0.1-hf-AWQ": 
    OPENAI_API_KEY = args.api_jwt
    OPENAI_CHAT_MODEL = "solidrust/Codestral-22B-v0.1-hf-AWQ"
    OPENAI_CHAT_API_URL = "https://isdm-chat.crocc.meso.umontpellier.fr/openai"
    llm = ChatOpenAI(
        model=OPENAI_CHAT_MODEL,
        openai_api_key=OPENAI_API_KEY,
        openai_api_base=OPENAI_CHAT_API_URL,
    )
    model_short_name = "codestral"
elif args.model == "mixtral:8x7b-instruct-v0.1-q5_0":
    from langchain_community.chat_models import ChatOllama

    LLM_MODEL = "mixtral:8x7b-instruct-v0.1-q5_0"
    LLM_JWT_BEARER = args.api_key
    LLM_API_URL = "https://chat.crocc.meso.umontpellier.fr/ollama"
    llm = ChatOllama(model=LLM_MODEL, base_url=LLM_API_URL,
    headers={"Authorization": "Bearer " + LLM_JWT_BEARER,"Content-Type":"application/json",})
    model_short_name = "mixtral"
else:
    from langchain_community.llms import Ollama
    MODEL = "llama3:8b"
    llm = Ollama(model=MODEL)
    model_short_name = "llama3"

logging.info(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name}: started')
# Define variables used for processing
#-------------------------------------
context = Context_GraphQL.context_GraphQL_RAG

file = "data/Queries.xlsx"
db = pd.read_excel(file)
parser = StrOutputParser()

# RAG: Retrieve similar questions based on the user's question
#-------------------------------------------------------------

input_file = "data/rag__DATA.xlsx"
df = pd.read_excel(input_file)

# Initialize the transformer model
model_mpnet = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
# Convert descriptions into vectors
df['vector'] = df['question'].apply(lambda description: model_mpnet.encode(description).astype('float32'))


# Setting up the Faiss index
#---------------------------

# Build the FAISS index
index = faiss.IndexFlatL2(len(df['vector'][0]))
vectors = np.array(df['vector'].tolist())
index.add(vectors)

# Transform the user input into a vector
def transform_user_input(user_input):
    return model_mpnet.encode(user_input).astype('float32')

# Search for similarities using FAISS
def search_similarities(vector, top_k=1):
    distances, indices = index.search(np.array([vector]), top_k)
    matches = [{'metadata': {'question': df['question'][i], 'query': df['GraphQL'][i]}} for i in indices[0]]
    return matches


# Agent 2 for in-context learning to generate the REST request
#--------------------------------------------------------------

def create_template_Agent2(top_k_matches):
    template = """ you are a API GraphQL expert, given the following USER_QUESTION and CONTEXT, Please construct a correct REQUEST !
    
    USER_QUESTION:
    --
    {user_input}
    --
    CONTEXT: 
    
    --
    {context} 
    
   
   #########################################################################################################

    some examples of question and their corresponding request
  
    """
    # Itérez sur les objets dans top_k_matches
    for match in top_k_matches:
        query = match['metadata']['query'].replace('{', '{{').replace('}', '}}')
        question = match['metadata']['question']
        template += f"""
        example question: {question}
        response: {query}
    """

   
    template += """

    IMPORTANT: If you unable to answer the question, respond with "I don't know.
    IMPORTANT: In the context you will find a list of IDs for the countries and regions that you should use if you have a question about countries or regions. Don't use any other resources.
    IMPORTANT: Return a GraphQL request without explanations or comments.

    """
    
    return template




def modele_llm(question, llm, parser, context, retries=3, delay=5):
    
    user_vector = transform_user_input(question)
    top_k_matches = search_similarities(user_vector, top_k=5)
    template = create_template_Agent2(top_k_matches)
    prompt = PromptTemplate.from_template(template)

    for attempt in range(retries):
        try:
            chain = prompt | llm | parser 
            result = chain.invoke({"context": context, "user_input": question})
            return result
        except ValueError as e:
            if '504 Gateway Time-out' in str(e):
                print(f"Attempt {attempt + 1} failed with timeout error. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(delay)  # Introduce a delay before retrying
    
    raise ValueError("Max retries exceeded with timeout errors.")

def clean_graphql_query(query_string):
    # Find the start of the query
    start_index = query_string.find("query Data")
    if start_index == -1:
        return None  # Return None if "query Data" is not found
    
    # Extract the relevant part of the string
    query_part = query_string[start_index:]
    
    # Initialize counters for braces
    open_braces = 0
    close_braces = 0
    end_index = -1
    
    # Iterate through the string to find matching braces
    for i, char in enumerate(query_part):
        if char == '{':
            open_braces += 1
        elif char == '}':
            close_braces += 1
        
        # Check if the number of opening and closing braces match
        if open_braces > 0 and open_braces == close_braces:
            end_index = i + 1  # Include the closing brace
            break
    
    # Return the cleaned query
    if end_index != -1:
        return query_part[:end_index].strip()
    
    return None  # Return None if there is no matching closing brace

# Return Response
def ChatBot_response( llm, parser, context, question):

    response = modele_llm(question, llm, parser, context, retries=3, delay=5)
    if response is None:
        response = modele_llm(question, llm, parser, context, retries=3, delay=5)

    response = clean_graphql_query(response)
    response = re.sub(r'\\', '', response) 
    return response


# Test the model
#--------------------------------------------------------

def response(data, llm, parser, context):
    data['response'] = ''
    for index, row in data.iterrows():
        question = row['question']
        try:
            response = ChatBot_response(llm, parser, context, question)
            logging.info(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name}: progress: {index}/{len(data)}')
        except Exception as e:
            logging.error(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name}: Inference error: {e}')
        counter = 0   
        max_attempts = 25     
        while response is None and counter < max_attempts:
            response = ChatBot_response(llm, parser, context, question)
            counter += 1
                    
        data.at[index, 'response'] = response
    try:
        directory_name = f"output/{current_time}_{hostname}"
        os.makedirs(directory_name, exist_ok=True)
        data.to_excel(f"{directory_name}/output_rag_graphql_{model_short_name}_{hostname}_{current_time}.xlsx", index=False)  
        logging.info(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name} Finished with {len(data)} queries processed')
    except Exception as e:
        logging.error(f'{str(__file__).split("/")[-1]}  | {args.model} Saving file: {e}')
    
response(db, llm, parser, context)
