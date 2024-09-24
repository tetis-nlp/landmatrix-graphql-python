import pandas as pd
import requests
import ast
import os
import re

# Charger les fichiers Excel
models = ['output_GraphQL_InContext_codestral.xlsx']


###################### Récupérer les réponses des requêtes GraphQL ##################

def graphQl(query):
    # Envoyer la requête à l'API GraphQL
    response = requests.post('https://land-matrix.teledetection.fr/landmatrix/graphql/', json={'query': query})
    
    # Vérifier le statut de la réponse
    if response.status_code == 200:
        # Convertir la réponse en format JSON
        data = response.json()
        return data  # Retourner les données JSON si la requête a réussi
    else:
        return None  # Retourner None si la requête a échoué
    

#######################  Ajouter les réponses JSON au fichier Excel ####################

def add_responses_to_excel(df):
    df['Real_Response'] = ''
    df['Predict_Response'] = ''

    for index, row in df.iterrows():
        real = str(row['Real_Query_GraphQL'])
        predict = str(row['Predict_Query'])  
        real_response = graphQl(real)
        predict_response = graphQl(predict)
        
        if real_response is not None:
            df.at[index, 'Real_Response'] = str(real_response)
        if predict_response is not None:
            df.at[index, 'Predict_Response'] = str(predict_response)

    return df


#################  Calculer la similarité en utilisant Jaccard Similarity ##########

def jaccard_similarity(doc1, doc2):
    # List the unique words in each document
    words_doc1 = set(doc1.lower().split())
    words_doc2 = set(doc2.lower().split())
    
    # Find the intersection of words between the two documents
    intersection = words_doc1.intersection(words_doc2)
    
    # Calculate Jaccard similarity score if the union set is not empty
    union = words_doc1.union(words_doc2)
    if len(union) != 0:
        return float(len(intersection)) / len(union)
    else:
        return 0  # Return 0 if both documents are empty
    

def jaccard_similarity_results(df):
    df_test = df.copy() 
    df_test["jaccard_score_result"] = ""  
    
    for index, row in df_test.iterrows():
        predict = row["Predict_Response"]
        true = row["Real_Response"]
        
        # Check if query or response is NaN, and handle accordingly
        if pd.isna(predict) or pd.isna(true):
            df_test.at[index, "jaccard_score_result"] = 0  # Assign a default score of 0 if either query or response is NaN
        else:
            # Calculate the Jaccard similarity between query and response
            df_test.at[index, "jaccard_score_result"] = jaccard_similarity(predict, true)
    
    return df_test

def jaccard_similarity_requests(df):
    df_test = df.copy() 
    df_test["jaccard_score_request"] = ""  
    
    for index, row in df_test.iterrows():
        predict = row["Predict_Query"]
        true = row["Real_Query_GraphQL"]
        
        # Check if query or response is NaN, and handle accordingly
        if pd.isna(predict) or pd.isna(true):
            df_test.at[index, "jaccard_score_request"] = 0  # Assign a default score of 0 if either query or response is NaN
        else:
            # Calculate the Jaccard similarity between query and response
            df_test.at[index, "jaccard_score_request"] = jaccard_similarity(predict, true)
    
    return df_test

###################### Vérifier la validité d'une requête GraphQL ###########################

def check_graphql_response(response):
    # Vérifie si la réponse contient des erreurs
    if "errors" in response or "error" in response :
        return 0  # Retourne 0 si des erreurs sont présentes dans la réponse
    elif "{'data': {'deals': []" in response:
        return 0
    else:
        return 1  # Retourne 1 si la réponse est valide
    

def valid_resultats(df):
    df_test = df.copy()  
    df_test["valid_query"] = ""
    
    for index, row in df_test.iterrows():
        predict = row["Predict_Response"]
        true = row["Real_Response"]
        
        # Vérifie si la requête ou la réponse est NaN, et gère en conséquence
        if pd.isna(predict):
            df_test.at[index, "valid_query"] = 0  # Attribue un score par défaut de 0 si la requête ou la réponse est NaN
        else:
            predict_score = check_graphql_response(predict)
            # Attribution des scores
            if predict_score == 0 :
                df_test.at[index, "valid_query"] = 0  # Attribution de 0 si l'une des réponses contient des erreurs
            if predict_score == 1 :
                df_test.at[index, "valid_query"] = 1  # Attribution de 1 si les réponses sont valides
    
    return df_test

########################## Fonctions pour la comparaison des entités ############################



def extract_filters(query):
    # Recherche des filtres dans la requête en utilisant une expression régulière
    filters = re.findall(r'{\s*field:\s*"([^"]+)"\s*,\s*operation:\s*([^,]+)\s*,\s*value:\s*([^}]+)\s*}', query)
    
    # Créer une liste de dictionnaires pour stocker les informations sur les filtres
    extracted_filters = []
    for filter_match in filters:
        field, operation, value = filter_match
        extracted_filters.append({'field': field.strip(), 'operation': operation.strip(), 'value': value.strip()})
    
    return extracted_filters



def compare_filters(query1, query2):
    # Extraire les filtres des deux requêtes
    filters_query1 = extract_filters(query1)
    filters_query2 = extract_filters(query2)
    
    # Initialiser des ensembles pour stocker les champs des filtres
    fields_query1 = set(filter1['field'] for filter1 in filters_query1)
    fields_query2 = set(filter2['field'] for filter2 in filters_query2)
    
    values_query  = set(filter1['value'] for filter1 in filters_query1)
    values_query2 = set(filter2['value'] for filter2 in filters_query2)
    
    # Créer des colonnes pour stocker les résultats
    TP = 0
    FP = 0
    FN = 0
    value = 0
    
    # Vérifier si les deux ensembles de champs sont égaux
    if fields_query1 == fields_query2:
        TP = 1
        if values_query == values_query2:
            value = 1
    
    # Vérifier si tous les champs de la première requête appartiennent à la deuxième requête
    elif fields_query1.issubset(fields_query2):
        FP = 1
        if values_query == values_query2:
            value = 1
    
    # Vérifier si un des champs de la première requête n'appartient pas à la deuxième requête
    else:
        FN = 1
        if values_query == values_query2:
            value = 1
    
    return TP, FP, FN, value

def fct_comparer_Filtre(df_test):
    df_test["TP"] = 0
    df_test["FP"] = 0
    df_test["FN"] = 0
    df_test["TP_value"] = 0
    
    # Iterate over each row in the DataFrame
    for index, row in df_test.iterrows():
        # Extract the query and response from the current row
        predict = row["Predict_Query"]
        true = row["Real_Query_GraphQL"]
        
        # Check if query or response is NaN, and handle accordingly
        if pd.isna(predict) or pd.isna(true):
            continue  # Skip if either query or response is NaN
        else:
            # Compare the filters of predicted and true queries
            TP, FP, FN, value= compare_filters(true, predict)
            df_test.at[index, "TP"] = TP
            df_test.at[index, "FP"] = FP
            df_test.at[index, "FN"] = FN
            df_test.at[index, "TP_value"] = value
    
    return df_test


########################### Métriques d'évaluation #################################

def calculate_metrics_return(df):

    true_positives  = df['TP'].sum()
    false_positives = df['FP'].sum()
    false_negatives = df['FN'].sum()
    mean_tp_value   = df['TP_value'].mean()
    
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    accuracy = true_positives / len(df)
    
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, accuracy, f1_score, mean_tp_value

#############################################################3


def data_result(model, moyenne_Jaccard_result, moyenne_Jaccard_request, moyenne_valid, precision, recall, accuracy, f1_score, mean_tp_value):
    # Création d'un DataFrame avec les nouvelles valeurs
    new_data = pd.DataFrame([{
        'Model_Name': model, 
        'Jaccard_Similarity_results': moyenne_Jaccard_result, 
        'Jaccard_Similarity_request': moyenne_Jaccard_request, 
        'Valid_Query': moyenne_valid, 
        'precision': precision, 
        'recall': recall, 
        'accuracy': accuracy, 
        'f1_score': f1_score,
        'tp_value_score': mean_tp_value
    }])
    
    file_path = 'Metrics_for_GraphQL.xlsx'
    
    # Vérifiez si le fichier existe déjà
    if os.path.exists(file_path):
        # Lire le fichier existant
        existing_data = pd.read_excel(file_path)
        # Concaténer les nouvelles données avec les données existantes
        df = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        # Si le fichier n'existe pas, utilisez simplement les nouvelles données
        df = new_data
    
    # Sauvegarder le DataFrame dans un fichier Excel
    df.to_excel(file_path, index=False)

    return df


###################################### Evaluation ###########################################

for model in models:
    df = pd.read_excel(model)

    # Appeler la fonction pour ajouter les réponses GraphQL au DataFrame
    df_reponse = add_responses_to_excel(df)

    # Calculer la similarité using Jaccard_Similarity
    jaccard_results  = jaccard_similarity_results(df_reponse)
    jaccard_requests = jaccard_similarity_requests(df_reponse)
    valid_query_result = valid_resultats(df_reponse)

    # Calculer la moyenne des scores
    average_similarity_result = jaccard_results['jaccard_score_result'].mean()
    average_similarity_request = jaccard_requests['jaccard_score_request'].mean()
    average_similarity_valid  = valid_query_result['valid_query'].mean()

    # Metrics d'évaluation
    data = fct_comparer_Filtre(df)
    precision, recall, accuracy, f1_score, mean_tp_value = calculate_metrics_return(data)

    # Appeler la fonction data_result pour ajouter les résultats au fichier Excel
    data_result(model, average_similarity_result, average_similarity_request, average_similarity_valid, precision, recall, accuracy, f1_score, mean_tp_value)
