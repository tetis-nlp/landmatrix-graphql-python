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

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
import pandas as pd
import re
from langchain_core.output_parsers import StrOutputParser
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import Context_REST
from langchain_openai import ChatOpenAI

from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

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
#--------------------------------------------------------
input_file = 'data/Queries.xlsx'
df = pd.read_excel(input_file)

### Construct the prompt
#-------------------------

parser = StrOutputParser()
context = Context_REST.context_for_InContext_learning
template = """
As a REST request expert, you'll create a syntactically correct REST query based on an input question.

In the context you have access to a relevant information from the landMatrix REST API documentation.
Utilize provided examples to generate a correct REST request.

IMPORTANT: If you unable to answer the question, respond with "I don't know."
IMPORTANT: In the context you will find a list of IDs for the countries and regions that you should use if you have a question about countries or regions. Don't use any other resources.
IMPORTANT: Return a REST request without explanations or comments.

Context: {context}

Question: {question}
"""

prompt = PromptTemplate.from_template(template)

### Generate responses
#---------------------

def modele(question,prompt,model,parser, context):

    chain = prompt | model | parser
    try:
        result = chain.invoke({"context": context, "question": question})
    except Exception as e:
        logging.error(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name}: Inference error: {e}')

    return result

def extract_first_rest_request(text):
    # Pattern to capture URLs with http or https surrounded by single quotes
    url_pattern = r"'(https?://[^\s']+)'"
    
    # Search for URLs in the text
    urls = re.findall(url_pattern, text)
    
    # Return the first URL found or None if no URL is found
    return urls[0] if urls else None

def add_responses_to_excel(df, prompt, model, parser, context):
    df['Predict_Query'] = ''

    for index, row in df.iterrows():
        question = row['question']
        response = modele(question, prompt, model, parser, context)
        while response is None:
            response = modele(question, prompt, model, parser, context)
        response = extract_first_rest_request(response)
        df.at[index, 'Predict_Query'] = response
    return df

### Load the results
#--------------------------

data_response = add_responses_to_excel(df, prompt, llm, parser, context)
try:
    data_response.to_excel(f"output/output_incontext_rest_{model_short_name}.xlsx", index=False)
    logging.info(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name} Finished with {len(data_response)} queries processed')
except Exception as e:
    logging.error(f'{str(__file__).split("/")[-1]}  | {args.model} Saving file: {e}')
