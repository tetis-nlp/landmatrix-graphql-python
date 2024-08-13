# Aide à l'interrogation GraphQL de la Land Matrix via Python
[![Land Matrix](https://landmatrix.org/images/lm-logo-dark.png)](https://landmatrix.org/)

Liens d'intérêt :
- [Documentation API Land Matrix](https://landmatrix.readthedocs.io/en/latest/api/)
- [Playground GraphQL Land Matrix](https://landmatrix.org/graphql/)

# 1. Interrogation Land Matrix via Python

Interrogation de la base de donnees land matrix via scripts python.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/TP1__GraphQl.ipynb)


# 2. Correction et alignement des noms de pays avec ceux de la Land Matrix

Ce programme calcule la similarité entre un nom de pays fourni en entrée et les noms de pays d'une liste existante, même en cas de fautes de frappe ou de noms incomplets. Il utilise des embeddings de mots pour représenter chaque nom de pays sous forme numérique, puis compare la similarité cosinus entre l'embedding du pays donné et ceux de la liste pour trouver la correspondance la plus proche. Cette méthode permet d'associer le pays donné à son homologue le plus similaire dans la liste, facilitant ainsi la recherche de correspondances.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/Corresponding_Similarity.ipynb)

# 3. Adapter les large language models (LLMs) using In-Context learning

Pour adapter les large language models (LLMs) tels que llama3 et mixtral, nous utilisons l'apprentissage en contexte (in-context learning) afin de générer des requêtes GraphQL correctes pour interroger la base de données Land Matrix.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/In_Context_Learning.ipynb)

# 4. Adapter les large language models (LLMs) pour la génération de requêtes REST en se basant sur des questions en langage naturel, en utilisant l'apprentissage contextuel (In-Context Learning), RAG et des agents LLM.

### --- Agents LLM ---

La première étape impliquait l'utilisation d’une fonction pour récupérer des informations externes à partir de la base de données LMI. Ces informations représentent les valeurs que les champs de la base peuvent prendre. En raison de la taille et de la complexité de la base de données, cette fonction a étéutilisée pour extraire les valeurs des champs pertinents pour chaque question.

Pour chaque question, les champs souhaités ont été extraits à l'aide d'un LLM, qui prend en entrée la question de l'utilisateur et retourne une liste des champs pertinents. La fonction envoie ensuite cette liste à l'API LMI pour récupérer les valeurs de ces champs. Ces valeurs sont ensuite utilisées dans le contexte d'un second LLM qui va générer les requêtes REST. L’utilisation de plusieurs LLMs pour l'extraction des champs pertinents et la génération des requêtes REST est un exemple d'approche multi-agents.

### --- RAG ---

Dans le cadre de l'amélioration de la qualité des requêtes REST générées par le modèle, nous avons utilisé l'approche du RAG pour enrichir le contexte du prompt avec des questions en langage naturel et leurs requêtes correspondantes similaires à la question d'entrée. Le processus commence par le calcul des embeddings des mots de la question d'entrée et des questions en langage naturel de notre corpus de questions-requêtes en utilisant le modèle
all-mpnet-base-v2. Ce modèle de sentence-transformers mappe les phrases et paragraphes dans un espace vectoriel dense de 768 dimensions, utile pour des tâches comme le clustering ou la recherche sémantique. Ensuite, nous avons utilisé Facebook AI Similarity Search (Faiss), une bibliothèque pour la recherche de similarité et le clustering de vecteurs denses. Faiss contient des algorithmes permettant la recherche dans des ensembles de vecteurs de toute taille, même ceux ne tenant pas en RAM, et inclut du code de support pour l'évaluation et l'ajustement des paramètres.

Nous calculons la similarité entre la question d'entrée et toutes les questions représentées par leurs embeddings stockés dans la base de données vectorielle. Nous retournons les k questions les plus similaires à la question d'entrée ainsi que leurs requêtes REST correspondantes pour les inclure dans le contexte. Plutôt que d'utiliser des requêtes aléatoires dans ce contexte, cette méthode consiste à enrichir le contexte avec des requêtes REST similaires à la question d'entrée. Cela permet au modèle de générer des requêtes qui sont à la fois syntaxiquement correctes et contextuellement pertinentes.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/REST_Request.ipynb)
