import requests
import pandas as pd
import ast
from urllib.parse import urlparse, parse_qs
import os



#### Charger les fichiers Excel à évaluer
#----------------------------------------

models = ["agent.xlsx","in_context_cs.xlsx","rag.xlsx", "in_context_ms.xlsx"]


###################### Récupérer les réponses des requêtes REST ###################

def REST(URL):
    url = URL
    headers = {
        'accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)

        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Récupérer les données JSON
            data = response.json()

            # Faire quelque chose avec les données
            return data  # Par exemple, afficher les données

        else:
            print(f"Erreur de requête: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion: {e}")

#######################  Ajouter les réponses au fichier Excel ####################

def add_responses_to_excel(df):
    df['Real_Response'] = ''
    df['Predict_Response'] = ''

    for index, row in df.iterrows():
        real = str(row['Real_Query_REST'])
        predict = str(row['Predict_Query'])  
        real_response = REST(real)
        predict_response = REST(predict)
        
        if real_response is not None:
            df.at[index, 'Real_Response'] = str(real_response)
        if predict_response is not None:
            df.at[index, 'Predict_Response'] = str(predict_response)

    return df


#################  Calculer la similarité utilisant Jaccard Similarity ##########

def jaccard_similarity_function(doc1, doc2):
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
    

def jaccard_similarity_for_results(df):
    data = df.copy() 
    data["jaccard_score"] = ""  
    
    for index, row in data.iterrows():
        predict = row["Predict_Response"]
        real = row["Real_Response"]
        
        # Check if query or response is NaN, and handle accordingly
        if pd.isna(predict) or pd.isna(real):
            data.at[index, "jaccard_score_result"] = 0  # Assign a default score of 0 if either query or response is NaN
        else:
            # Calculate the Jaccard similarity between query and response
            data.at[index, "jaccard_score_result"] = jaccard_similarity_function(predict, real)
    
    return data


def jaccard_similarity_for_queries(df):
    data = df.copy() 
    data["jaccard_score"] = ""  
    
    for index, row in data.iterrows():
        predict = row["Predict_Query"]
        real = row["Real_Query_REST"]
        
        # Check if query or response is NaN, and handle accordingly
        if pd.isna(predict) or pd.isna(real):
            data.at[index, "jaccard_score_query"] = 0  # Assign a default score of 0 if either query or response is NaN
        else:
            # Calculate the Jaccard similarity between query and response
            data.at[index, "jaccard_score_query"] = jaccard_similarity_function(predict, real)
    
    return data


####################### Valid query #########################################

def Valid_REST(URL):
    url = URL
    headers = {
        'accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)

        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Récupérer les données JSON
            data = response.json()

        else:
            print(f"Erreur de requête: {response.status_code}")
            return 500

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion: {e}")

# Fonction pour calculer les erreurs 500 sur un corpus
def Valid_REST_fct(df):
    data = df.copy()  # Copier les données pour ne pas modifier l'original
    data["valid_query"] = 0  # Ajouter une colonne pour stocker les erreurs 500

    for index, row in data.iterrows():
        url = row["Predict_Query"]  # Remplacer par le nom de la colonne qui contient les URLs

        # Vérifier si l'URL est NaN et gérer en conséquence
        if pd.isna(url):
            data.at[index, "valid_query"] = 0  # Assigner 0 si l'URL est manquante
        else:
            resultat = Valid_REST(url)  # Appeler la fonction REST pour vérifier la réponse
            if resultat == 500:
                data.at[index, "valid_query"] = 0  # Ajouter 1 si on trouve une erreur 500
            else:
                data.at[index, "valid_query"] = 1  # Ajouter 0 sinon

    return data

##################################### Métriques d'évaluation des filtres ############################################################

def extract_filters(url):
    # Parse l'URL pour obtenir la chaîne de requête
    parsed_url = urlparse(url)
    # Extraire les paramètres sous forme de dictionnaire
    query_params = parse_qs(parsed_url.query)
    
    # Créer une liste de dictionnaires pour stocker les informations sur les filtres
    extracted_filters = []
    for key, value in query_params.items():
        # Ajouter un dictionnaire avec 'field' et 'value'
        extracted_filters.append({
            'field': key.strip(),
            'value': value[0].strip()  # On prend le premier élément car les valeurs sont toujours des listes
        })
    
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
    
    # Vérifier si un des champs de la première requête n'appartient pas à la deuxième requête
    else:
        FN = 1
        
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
        real = row["Real_Query_REST"]
        
        # Check if query or response is NaN, and handle accordingly
        if pd.isna(predict) or pd.isna(real):
            continue  # Skip if either query or response is NaN
        else:
            # Compare the filters of predicted and true queries
            TP, FP, FN, value= compare_filters(real, predict)
            df_test.at[index, "TP"] = TP
            df_test.at[index, "FP"] = FP
            df_test.at[index, "FN"] = FN
            df_test.at[index, "TP_value"] = value
    
    return df_test

def calculate_metrics(df):

    true_positives  = df['TP'].sum()
    false_positives = df['FP'].sum()
    false_negatives = df['FN'].sum()
    mean_tp_value   = df['TP_value'].mean()
    
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    accuracy = true_positives / (true_positives + false_negatives + false_positives)
    
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, accuracy, f1_score, mean_tp_value

###########################################################################################

def metrics_result(model, moyenne_Jaccard_result, moyenne_Jaccard_query, moyenne_valid, precision, recall, accuracy, f1_score, mean_tp_value):
    # Création d'un DataFrame avec les nouvelles valeurs
    new_data = pd.DataFrame([{
        'model_name': model, 
        'moyenne_Jaccard_result': moyenne_Jaccard_result, 
        'moyenne_Jaccard_query': moyenne_Jaccard_query, 
        'moyenne_valid': moyenne_valid, 
        'precision': precision, 
        'recall': recall, 
        'accuracy': accuracy, 
        'f1_score': f1_score,
        'mean_tp_value': mean_tp_value
    }])
    
    file_path = 'Metrics_REST.xlsx'
    
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

#----------------------------- Evaluation ---------------------------------------------


for model in models:

    df = pd.read_excel(model)
    df_reponse = add_responses_to_excel(df)

    # Calculer la similarité entre les réponses réelles et générées 
    data_result  = jaccard_similarity_for_results(df_reponse)
    average_similarity_results = data_result['jaccard_score_result'].mean()

    # Calculer la similarité entre les réponses réelles et générées 
    data_queries = jaccard_similarity_for_queries(df_reponse)
    average_similarity_queries = data_queries['jaccard_score_query'].mean()
    
    data_valid = Valid_REST_fct(df_reponse)
    average_similarity_valid  = data_valid['valid_query'].mean()

    # Metrics d'évaluation
    data = fct_comparer_Filtre(df)
    precision, recall, accuracy, f1_score, mean_tp_value = calculate_metrics(data)

    # Appeler la fonction data_result pour ajouter les résultats au fichier Excel
    metrics_result(model, average_similarity_results, average_similarity_queries, average_similarity_valid, precision, recall, accuracy, f1_score, mean_tp_value)
