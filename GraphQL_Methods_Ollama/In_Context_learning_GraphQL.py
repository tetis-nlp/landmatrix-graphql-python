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


#--------------------------llama3:8b--ollama--------------------

from langchain_community.llms import Ollama
MODEL = "llama3:8b"
llm = Ollama(model=MODEL)

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
