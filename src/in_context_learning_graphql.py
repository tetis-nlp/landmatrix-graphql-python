import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--api_key', type=str, required=True, help='Your ISDM OpenAI API like Key')
parser.add_argument('--api_jwt', type=str, required=True, help='Your ISDM JWT')
parser.add_argument('--model', type=str, default="solidrust/Codestral-22B-v0.1-hf-AWQ")
args = parser.parse_args()

import time
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
import socket
from datetime import datetime
hostname = socket.gethostname()
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
import Context_GraphQL
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
context = Context_GraphQL.context_GraphQL_InContext

template = """
As a GraphQL expert, you'll create a syntactically correct GraphQL query based on an input question.

You have access to the schema of the GraphQL database and relevant information from the landMatrix GraphQL API documentation.
Utilize provided examples to generate the correct GraphQL request.

IMPORTANT: If you unable to answer the question, respond with "I don't know."
IMPORTANT: In the context you will find a list of IDs for the countries and regions that you should use if you have a question about countries or regions. Don't use any other resources.
IMPORTANT: Return just a GraphQL request without any other sentence.

Context: {context}

Question: {question}
"""

prompt = PromptTemplate.from_template(template)

### Generate responses
#---------------------

def modele(question, prompt, model, parser, context, retries=3, delay=5):
    chain = prompt | model | parser
    
    for attempt in range(retries):
        try:
            result = chain.invoke({"context": context, "question": question})
            return result
        except ValueError as e:
            # Handle the 504 Gateway Time-out error
            if '504 Gateway Time-out' in str(e):
                logging.error(f"Attempt {attempt + 1} failed with timeout error. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                logging.error(f'Unexpected error: {e}')
                raise  # Re-raise the error if it's not a timeout error
        except Exception as e:
            # Log other exceptions
            logging.error(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name}: Inference error: {e}')
            time.sleep(delay)  # Introduce a delay before retrying
    
    # Raise an exception after max retries are exceeded
    raise ValueError("Max retries exceeded with timeout errors.")

def add_responses_to_excel(df, prompt, model, parser, context):
    df['Predict_Query'] = ''

    for index, row in df.iterrows():
        question = row['question']
        response = modele(question, prompt, model, parser, context, retries=3, delay=5)
        response = re.sub(r'\\', '', response)
        while response is None:
            response = modele(question, prompt, model, parser, context, retries=3, delay=5)
            response = re.sub(r'\\', '', response)
        df.at[index, 'Predict_Query'] = response
    return df

### Load the results
#--------------------------

data_response = add_responses_to_excel(df, prompt, llm, parser, context)
try:
    directory_name = f"output/{current_time}_{hostname}"
    os.makedirs(directory_name, exist_ok=True)
    data_response.to_excel(f"{directory_name}/output_incontext_graphql_{model_short_name}_{hostname}_{current_time}.xlsx", index=False)
    logging.info(f'{str(__file__).split("/")[-1]} | {args.model} | {model_short_name} Finished with {len(data_response)} queries processed')
except Exception as e:
    logging.error(f'{str(__file__).split("/")[-1]}  | {args.model} Saving file: {e}')
