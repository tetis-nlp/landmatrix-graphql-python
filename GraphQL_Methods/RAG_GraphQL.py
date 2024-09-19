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
import Context_GraphQL
import faiss
import numpy as np
import time



# Set the environment variables from shell environment
#------------------Codestral-----------------------------------

OPENAI_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyMjkxNDgxLTU4NDItNDlkNi1iMjhkLTFmZDZjZWYwYjkzMiJ9.hOf578efg-7uV0sQCKVb_WIU9t5DKVoyspoU3vYV_yI"
OPENAI_CHAT_MODEL = "solidrust/Codestral-22B-v0.1-hf-AWQ"
OPENAI_CHAT_API_URL = "https://isdm-chat.crocc.meso.umontpellier.fr/openai"
llm = ChatOpenAI(
    model=OPENAI_CHAT_MODEL,
    openai_api_key=OPENAI_API_KEY,
    openai_api_base=OPENAI_CHAT_API_URL,
)

#---------------------mixtral----------------

# from langchain_community.chat_models import ChatOllama

# LLM_MODEL = "mixtral:8x7b-instruct-v0.1-q5_0"
# LLM_JWT_BEARER = "YOUR_API_KEY"
# LLM_API_URL = "https://chat.crocc.meso.umontpellier.fr/ollama"

# llm = ChatOllama(model=LLM_MODEL, base_url=LLM_API_URL,
# headers={"Authorization": "Bearer " + LLM_JWT_BEARER,"Content-Type":"application/json",})

#--------------------------llama3:8b--ollama--------------------

# from langchain_community.llms import Ollama
# MODEL = "llama3:8b"
# llm = Ollama(model=MODEL)

# Define variables used for processing
#-------------------------------------
context = Context_GraphQL.context_GraphQL_RAG

# RAG: Retrieve similar questions based on the user's question
#-------------------------------------------------------------

input_file = "rag__DATA.xlsx"
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


# Return Response
def ChatBot_response( llm, parser, context, question):

    response = modele_llm(question, llm, parser, context, retries=3, delay=5)
    if response is None:
        response = modele_llm(question, llm, parser, context, retries=3, delay=5)
        
    return response


# Test the model
#--------------------------------------------------------

file = "Queries_GraphQL.xlsx"
db = pd.read_excel(file)
parser = StrOutputParser()

def response(data, llm, parser, context):
    data['response'] = ''
    for index, row in data.iterrows():
        question = row['question']
        response = ChatBot_response(llm, parser, context, question)
        counter = 0   
        max_attempts = 25     
        while response is None and counter < max_attempts:
            response = ChatBot_response(llm, parser, context, question)
            counter += 1
                    
        data.at[index, 'response'] = response
    data.to_excel("OUTPUT_RAG_GraphQL.xlsx", index=False)  
    
response(db, llm, parser, context)
