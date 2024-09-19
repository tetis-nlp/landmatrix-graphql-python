from langchain.prompts import PromptTemplate
import pandas as pd
from langchain_core.output_parsers import StrOutputParser
import Context_REST
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
import re

#--------------------------llama3:8b--ollama--------------------

from langchain_community.llms import Ollama
MODEL = "llama3:8b"
llm = Ollama(model=MODEL)

#--------------------------------------------------------
input_file = 'Queries.xlsx'
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
    result = chain.invoke({"context": context, "question": question})

    return result

def add_responses_to_excel(df, prompt, model, parser, context):
    df['Predict_Query'] = ''

    for index, row in df.iterrows():
        question = row['question']
        response = modele(question, prompt, model, parser, context)
        while response is None:
            response = modele(question, prompt, model, parser, context)
        df.at[index, 'Predict_Query'] = response
    return df

### Load the results
#--------------------------

data_response = add_responses_to_excel(df, prompt, model, parser, context)
data_response.to_excel("OUTPUT_InContext.xlsx", index=False)
