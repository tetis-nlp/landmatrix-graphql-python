import pandas as pd
import Functions

# Charger le fichier Excel
models = ['output_llama.xlsx', 'llama.xlsx', 'output_mixtral.xlsx', 'mixtral.xlsx']
# models = ['output_test_RAG_.xlsx']

for model in models:
    df = pd.read_excel(model)
    df = df.drop(df.tail(7).index)

    # Appeler la fonction pour ajouter les réponses GraphQL au DataFrame
    df_reponse = Functions.add_responses_to_excel(df)

    # Calculer la similarité entre les réponses réelles et générées using Jaccard_Similarity
    data = Functions.jaccard_similarity_resultats(df_reponse)
    data = Functions.valid_resultats(data)

    # Calculer la moyenne des scores
    average_similarity_result = data['jaccard_score'].mean()
    average_similarity_valid  = data['valid_query'].mean()

    # Metrics d'évaluation
    data_ET = Functions.fct_comparer_Filtre(df)
    precision, recall, accuracy, f1_score, mean_tp_value = Functions.calculate_metrics_return(data_ET)

    # Appeler la fonction data_result pour ajouter les résultats au fichier Excel
    Functions.data_result(model, average_similarity_result, average_similarity_valid, precision, recall, accuracy, f1_score, mean_tp_value)
