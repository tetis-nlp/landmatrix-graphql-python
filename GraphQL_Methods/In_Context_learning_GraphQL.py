from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
import pandas as pd
import re
from langchain_core.output_parsers import StrOutputParser
import Context_GraphQL
from langchain_openai import ChatOpenAI

from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

# Set the environment variables from shell environment
#------------------Codestral-----------------------------------

# OPENAI_API_KEY = "YOUR_KEY"
# OPENAI_CHAT_MODEL = "solidrust/Codestral-22B-v0.1-hf-AWQ"
# OPENAI_CHAT_API_URL = "https://isdm-chat.crocc.meso.umontpellier.fr/openai"
# llm = ChatOpenAI(
#     model=OPENAI_CHAT_MODEL,
#     openai_api_key=OPENAI_API_KEY,
#     openai_api_base=OPENAI_CHAT_API_URL,
# )

#---------------------mixtral----------------

from langchain_community.chat_models import ChatOllama

LLM_MODEL = "mixtral:8x7b-instruct-v0.1-q5_0"
LLM_JWT_BEARER = "YOUR_KEY"
LLM_API_URL = "https://chat.crocc.meso.umontpellier.fr/ollama"

llm = ChatOllama(model=LLM_MODEL, base_url=LLM_API_URL,
headers={"Authorization": "Bearer " + LLM_JWT_BEARER,"Content-Type":"application/json",})


#--------------------------------------------------------
input_file = 'Queries_GraphQL.xlsx'
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

def modele(question,prompt,model,parser, context):

    chain = prompt | model | parser
    result = chain.invoke({"context": context, "question": question})

    return result

def add_responses_to_excel(df, prompt, model, parser, context):
    df['Predict_Query'] = ''

    for index, row in df.iterrows():
        question = row['question']
        response = modele(question, prompt, model, parser, context)
        response = re.sub(r'\\', '', response)
        while response is None:
            response = modele(question, prompt, model, parser, context)
            response = re.sub(r'\\', '', response)
        df.at[index, 'Predict_Query'] = response
    return df

### Load the results
#--------------------------

data_response = add_responses_to_excel(df, prompt, llm, parser, context)
data_response.to_excel("output_GraphQL_InContext.xlsx", index=False)
