import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--api_key', type=str, required=True, help='Your ISDM OpenAI API like Key')
parser.add_argument('--api_jwt', type=str, required=True, help='Your ISDM JWT')
parser.add_argument('--model', type=str, default="solidrust/Codestral-22B-v0.1-hf-AWQ")
args = parser.parse_args()

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
import json
from transformers import AutoTokenizer, RobertaModel
from sentence_transformers import SentenceTransformer
import torch
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import Context_GraphQL
import faiss
import numpy as np
import time
from tqdm import tqdm

if args.model == "solidrust/Codestral-22B-v0.1-hf-AWQ": 
    OPENAI_API_KEY = args.api_key
    OPENAI_CHAT_MODEL = "solidrust/Codestral-22B-v0.1-hf-AWQ"
    OPENAI_CHAT_API_URL = "https://isdm-chat.crocc.meso.umontpellier.fr/openai"
    llm = ChatOpenAI(
        model=OPENAI_CHAT_MODEL,
        openai_api_key=OPENAI_API_KEY,
        openai_api_base=OPENAI_CHAT_API_URL,
    )
elif args.model == "mixtral:8x7b-instruct-v0.1-q5_0":
    from langchain_community.chat_models import ChatOllama

    LLM_MODEL = "mixtral:8x7b-instruct-v0.1-q5_0"
    LLM_JWT_BEARER = args.api_jwt
    LLM_API_URL = "https://chat.crocc.meso.umontpellier.fr/ollama"
    llm = ChatOllama(model=LLM_MODEL, base_url=LLM_API_URL,
    headers={"Authorization": "Bearer " + LLM_JWT_BEARER,"Content-Type":"application/json",})
else:
    from langchain_community.llms import Ollama
    MODEL = "llama3:8b"
    llm = Ollama(model=MODEL)

# Define variables used for processing
#-------------------------------------
context = Context_GraphQL.context_Agent
data    = json.loads(context)
regions = Context_GraphQL.regions
countries = Context_GraphQL.countries

file = "data/Queries_GraphQL.xlsx"
db = pd.read_excel(file)
parser = StrOutputParser()

# Agent 1 for Entity extraction
#-------------------------------
def template_agent1():
    template = """
    {context}
    input question: {question}

    You are an entity extraction expert. Given an input question, you must identify the entities present in the question based on the values I provide. Return only the entities that exist in the input question in a list format.

    The entity type current_intention takes only these values: [Agriculture, Forestry, CONVERSATION, Renewable energy power plants, INDUSTRY, LAND_SPECULATION, MINING, OIL_GAS_EXTRACTION, TOURISM]

    The entity type crops takes only these values: ["Accacia", "Alfalfa", "Seaweed", "Macroalgae", "Almond", "Aloe Vera", "Apple", "Aquaculture", "Bamboo", "Banana", "Bean", "Bottle Gourd", "Barley", "Buckwheat", "Cacao", "Cassava", "Cashew", "Chat", "Cherries", "Canola", "Coconut", "Coffee Plant", "Cotton", "Cereals", "Corn (Maize)", "Croton", "Castor Oil Plant", "Citrus Fruits", "Dill", "Eucalyptus", "Flowers", "Fig-Nut", "Fodder Plants", "Food crops", "Fruit", "Grapes", "Grains", "Herbs", "Jatropha", "Lentils", "Mango", "Mustard", "Oats", "Oil Seeds", "Oleagionous plant", "Olives", "Onion", "Oil Palm", "Other crops", "Palms", "Papaya", "Passion fruit", "Peanut (groundnut)", "Pepper", "Peas", "Pine", "Pineapple", "Pulses", "Pomegranate", "Pongamia Pinnata", "Potatoes", "Rapeseed", "Rice", "Rice", "Roses", "Rubber tree", "Rye", "Seeds Production", "Sesame", "Sorghum", "Soya Beans", "soy", "Spices", "Sisal", "Sugar beet", "Sugar Cane", "Sugar", "Sun Flower", "Sweet Potatoes", "Tobacco", "Tea", "Teff", "Teak", "Tomatoes", "Trees", "Vegetables", "Vineyard", "Wheat", "Yam"]

    The entity type implementation_status takes only these values: [project not started, startup phase, in operation, project abandoned]

    The entity type mineral_resources takes only these values: ["Aluminum", "Asphaltite", "Anthracite", "Barite", "Basalt", "Bauxite", "Bentonite", "Building materials", "Carbon", "Chromite", "Clay", "Coal", "Cobalt", "Copper", "Diamonds", "Emerald", "Feldspar", "Fluoride", "Gas", "Gold", "Granite", "Gravel", "Heavy Mineral Sands", "Ilmenite", "Iron", "Jade", "Lead", "Limestone", "Lithium", "Magnetite", "Molybdenum", "Manganese", "Marble", "Nickel", "Petroleum", "Phosphorous", "Platinum", "Hydrocarbons", "crude oil", "Pyrolisis Plant", "Rutile", "Sand", "Silica", "Silver", "Salt", "Stone", "Tin", "Titanium", "Uranium", "Zinc"]

    The entity type animals takes only these values: ["Aquaculture (animals)", "Beef Cattle", "Cattle", "Dairy Cattle", "Fish", "Goats", "Other livestock", "Pork", "Poultry", "Sheep", "Shrimp"]

    The entity type negative_impacts takes only these values: [Environmental degradation, Socio-economic, Cultural loss, Eviction, Displacement, Violence]

    The entity type former_land_cover takes only these values: [Cropland, Forest land, Pasture, Shrub land/Grassland (Rangeland), Marginal land, Wetland]

    The entity nature_of_deal takes only these values: [Outright purchase, Lease, Concession, Exploitation permit / license / concession (for mineral resources), Pure contract farming]

    The entity type Regions takes only these values: [Africa, Oceania, Northern America, Asia, Eastern Europe, Latin America and the Caribbean]

    Entity: Country

    Entity: year

    ################################################################################################################################

    Expected result must be in list format like this: ["entity1" : "value", "entity2", "value"]. Return just a list and nothing else.
    
    For example:
        input question: What types of investment in Forestry exist in Morocco in 2010?
        expected result: ["current_intention": "Forestry", "Country": "Morocco", "year": "2010"]
        
    #################################################################################################################################
    
    if you have more than value for a single entity, expected result must be like what we did with this example: 
    question: "What types of investment exist in Africa and Asia?" 
    response: ["Region": "Africa", "Region": "Asia"]


    IMPORTANT: However, since the question does not specify the type of investment (such as Agriculture, Forestry, MINING, etc.), no "current_intention" entity is included in the response.
    IMPORTANT: Do not hallucination !
        """
    prompt = PromptTemplate.from_template(template)
    return prompt



def clean_Output_Agent1(result):
    # Using a regular expression to extract the list
    match = re.sub(r'\\', '', result)
    match = re.search(r"\[.*?\]", match)
    if match is None:
        return None

    list_str = match.group()

    output_string = list_str.replace("[", "{").replace("]", "}")
    output_string = output_string.replace("'", '"')
    output_string = output_string.replace("None", "null")

    try:
        data_dict = json.loads(output_string)
    except json.JSONDecodeError:
        return None

    return data_dict


# Receive the information of entities extracted by the first Agent
#-----------------------------------------------------------------
def FormFields(entity):
    list = []
    if entity == "current_intention":
        entity = "current_intention_of_investment"
    if entity == "animals":
        entity = "current_animals"
    if entity == "mineral_resources":
        entity = "current_mineral_resources"
    if entity == "crops":
        entity = "current_crops"
    if entity == "implementation_status":
        entity = "current_implementation_status"  
    if entity == "current_intention_of_investment" or entity == "nature_of_deal" or entity == "former_land_cover" or entity == "negative_impacts" or entity == "current_animals" or entity == "current_mineral_resources" or entity == "current_implementation_status" or entity == "current_crops":
        for choice in data["data"]["formfields"]["deal"][entity]["choices"]:
            name  = entity
            type  = choice["label"]
            value = choice["value"]
            list.append(f"[champs: {name}, label: {type}, value:{value}]")
            
    return list

# Correction of countries and regions using Similarity
#-----------------------------------------------------

model_name = "roberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = RobertaModel.from_pretrained(model_name)
def word_embedding(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    with torch.no_grad():
        last_hidden_states = model(input_ids).last_hidden_state
    return last_hidden_states.mean(dim=1)[0]

# Calculate the word embedding for the country and region

def calculate_word_embeddings(countries):

    for country in countries:
        countrie = country['country.name'].lower()
        country_embedding = word_embedding(countrie)
        country['country_embedding'] = country_embedding

    return countries


def calculate_word_embeddings_regions(regions):

    for region in regions:
        reg = region['region.name'].lower()
        region_embedding = word_embedding(reg)
        region['region_embedding'] = region_embedding

    return regions

countries = calculate_word_embeddings(countries)
regions = calculate_word_embeddings_regions(regions)



# Calculate the similarity 
#---------------------------

def similarities_Country(input_word):
    # Initialize the maximum similarity and the corresponding word
    max_similarity = -1
    most_similar_word = None
    id = None

    # Obtain the embedding of the input word
    input_word = input_word.lower()
    input_embedding = word_embedding(input_word)

    # Iterate over each country in the list
    for country in countries:
        # Compute the cosine similarity between the input word and the current country
        similarity = cosine_similarity([input_embedding], [country['country_embedding']])

        # Update the maximum similarity and the corresponding word if the current similarity is greater
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_word = country["country.name"]
            id = country["id"]

    return most_similar_word

def similarities_region(input_word):
    # Initialize the maximum similarity and the corresponding word
    max_similarity = -1
    most_similar_word = None
    id = None

    # Obtain the embedding of the input word
    input_word = input_word.lower()
    input_embedding = word_embedding(input_word)

    # Iterate over each region in the list
    for region in regions:
        # Compute the cosine similarity between the input word and the current region
        similarity = cosine_similarity([input_embedding], [region['region_embedding']])

        # Update the maximum similarity and the corresponding word if the current similarity is greater
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_word = region["region.name"]
            id = region["id"]

    return most_similar_word

def Country(country_name):
    list = []
    for country in countries:
        if country['country.name'] == country_name:
            country_id = country['id']
            list.append(f"[country.id: {country_id}, country.name:{country_name}]")
    return list

def Region(region_name):
    list = []
    for region in regions:
        if region['region.name'] == region_name:
            region_id = region['id']
            list.append(f"[ region.id: { region_id}, region.name:{region_name}]")
    return list


nlp = spacy.load("en_core_web_sm")

def extract_countries(text,nlp):
    # Traiter le texte avec spacy
    doc = nlp(text)
    # Extraire les entités nommées de type 'GPE' (Geopolitical Entity)
    countries = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return countries

def Recevoir_Entities(data_dict, question):
    all_values = []
    # Vérifier l'existence des nœuds et récupérer leurs propriétés
    for entity, value in data_dict.items():
        if value != None :
            if entity == 'Country' :
                value = value.lower()
                Similar_Country = similarities_Country(value)
                if Similar_Country != None:
                        Similar_Country = Country(Similar_Country)
                        if Similar_Country:
                            all_values.append(Similar_Country)
                if question:
                    countries = extract_countries(question,nlp)
                    for country in countries:
                        country = country.lower()
                        Country_name2 = similarities_Country(country)
                        if Country_name2 is not None and Country_name2 != Similar_Country:
                            result = Country(Country_name2)
                            if result:
                                all_values.append(result)
                        else: continue
            
            elif entity == 'Region' or entity == 'Regions':
                region_name = value.lower()
                Similar_Region = similarities_region(region_name)
                result = Region(Similar_Region)
                if result:
                    all_values.append(result)   
                    
            elif entity == "current_intention" or entity == "implementation_status" or entity == "crops" or entity == "animals" or entity == "minerals" or entity == "nature_of_deal" or entity == "negative_impacts" or entity == "former_land_cover" or entity == "Agriculture" or entity == "Forestry" or entity == "MINING":
                if value != "INVESTMENT":
                    FormField = FormFields(entity)
                    all_values.append(FormField)
            
            else : continue
        
    return all_values



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

def create_template_Agent2(top_k_matches, all_values, data_dict):
    template = """ You are an API GraphQL expert, given the following USER_QUESTION and CONTEXT, Please construct a correct REQUEST !
    
    USER_QUESTION:
    --
    {user_input}
    --
    CONTEXT: 
    
    --
    {context} 
    
    #######################################################################################################
    This list is so so important, it contain the values of the attributes that you will use in the GraphQL request
    
    """
    data_dict
    """
    
    """
    for value in all_values:
        template += f"""
        {value}
    """
    template += """
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

    Attention: do not return an empty result   
    """
    
    return template


def model_extraction(question, llm):
    parser = StrOutputParser()
    prompt = template_agent1()
    Agent = prompt | llm | parser 
    result = Agent.invoke({"context": "", "question": question})
    return result

def modele_llm(question, llm, parser, retries=3, delay=5):
    data_dict = model_extraction(question, llm)
    
    # Retry if data_dict is empty or None
    if not data_dict or data_dict == [] or data_dict == "": # while
        data_dict = model_extraction(question, llm)
        # time.sleep(delay)  # Introduce a delay between retries
    
    data_dict = clean_Output_Agent1(data_dict)
    
    if data_dict:
        all_values = Recevoir_Entities(data_dict, question)
    else:
        all_values = "___"  # Placeholder for no data scenario
    
    user_vector = transform_user_input(question)
    top_k_matches = search_similarities(user_vector, top_k=3)
    template = create_template_Agent2(top_k_matches, all_values, data_dict)
    prompt = PromptTemplate.from_template(template)

    for attempt in range(retries):
        try:
            chain = prompt | llm | parser 
            result = chain.invoke({"context": "", "user_input": question})
            return result, data_dict, all_values
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
def ChatBot_response( llm, parser,question):

    response, entities, all_values = modele_llm(question, llm, parser, retries=3, delay=5)
    if response is None:
        response, entities, all_values = modele_llm(question, llm, parser, retries=3, delay=5)
        
    response = re.sub(r'\\', '', response)
        
    return response


# Test the model
#-------------------------------------------------------

def response(data, llm, parser):
    data['Predict_Query'] = ''
    for index, row in tqdm(data.iterrows(), total=len(data)):
        question = row['question']
        response = ChatBot_response(llm, parser, question)
        counter = 0   
        max_attempts = 25     
        while response is None and counter < max_attempts:
            response = ChatBot_response(llm, parser, question)
            counter += 1
                    
        data.at[index, 'Predict_Query'] = response
    data.to_excel("output/OUTPUT_AGENT.xlsx", index=False)  
    
response(db, llm, parser)



