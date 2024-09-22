# Aide à l'interrogation GraphQL de la Land Matrix via Python
[![Land Matrix](https://landmatrix.org/images/lm-logo-dark.png)](https://landmatrix.org/)

Liens d'intérêt :
- [Documentation API Land Matrix](https://landmatrix.readthedocs.io/en/latest/api/)
- [Playground GraphQL Land Matrix](https://landmatrix.org/graphql/)

## 1. Interrogation Land Matrix via Python

Interrogation de la base de donnees land matrix via scripts python.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/TP1__GraphQl.ipynb)


## 2. Correction et alignement des noms de pays avec ceux de la Land Matrix

Ce programme calcule la similarité entre un nom de pays fourni en entrée et les noms de pays d'une liste existante, même en cas de fautes de frappe ou de noms incomplets. Il utilise des embeddings de mots pour représenter chaque nom de pays sous forme numérique, puis compare la similarité cosinus entre l'embedding du pays donné et ceux de la liste pour trouver la correspondance la plus proche. Cette méthode permet d'associer le pays donné à son homologue le plus similaire dans la liste, facilitant ainsi la recherche de correspondances.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/Corresponding_Similarity.ipynb)

## 3. Adapter les large language models (LLMs) using In-Context learning

Pour adapter les large language models (LLMs) tels que llama3 et mixtral, nous utilisons l'apprentissage en contexte (in-context learning) afin de générer des requêtes GraphQL correctes pour interroger la base de données Land Matrix.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/In_Context_Learning.ipynb)

## 4. Adapter les large language models (LLMs) pour la génération de requêtes REST en se basant sur des questions en langage naturel, en utilisant l'apprentissage contextuel (In-Context Learning), RAG et des agents LLM.

### --- Agents LLM ---

La première étape impliquait l'utilisation d’une fonction pour récupérer des informations externes à partir de la base de données LMI. Ces informations représentent les valeurs que les champs de la base peuvent prendre. En raison de la taille et de la complexité de la base de données, cette fonction a étéutilisée pour extraire les valeurs des champs pertinents pour chaque question.

Pour chaque question, les champs souhaités ont été extraits à l'aide d'un LLM, qui prend en entrée la question de l'utilisateur et retourne une liste des champs pertinents. La fonction envoie ensuite cette liste à l'API LMI pour récupérer les valeurs de ces champs. Ces valeurs sont ensuite utilisées dans le contexte d'un second LLM qui va générer les requêtes REST. L’utilisation de plusieurs LLMs pour l'extraction des champs pertinents et la génération des requêtes REST est un exemple d'approche multi-agents.

### --- RAG ---

Dans le cadre de l'amélioration de la qualité des requêtes REST générées par le modèle, nous avons utilisé l'approche du RAG pour enrichir le contexte du prompt avec des questions en langage naturel et leurs requêtes correspondantes similaires à la question d'entrée. Le processus commence par le calcul des embeddings des mots de la question d'entrée et des questions en langage naturel de notre corpus de questions-requêtes en utilisant le modèle
all-mpnet-base-v2. Ce modèle de sentence-transformers mappe les phrases et paragraphes dans un espace vectoriel dense de 768 dimensions, utile pour des tâches comme le clustering ou la recherche sémantique. Ensuite, nous avons utilisé Facebook AI Similarity Search (Faiss), une bibliothèque pour la recherche de similarité et le clustering de vecteurs denses. Faiss contient des algorithmes permettant la recherche dans des ensembles de vecteurs de toute taille, même ceux ne tenant pas en RAM, et inclut du code de support pour l'évaluation et l'ajustement des paramètres.

Nous calculons la similarité entre la question d'entrée et toutes les questions représentées par leurs embeddings stockés dans la base de données vectorielle. Nous retournons les k questions les plus similaires à la question d'entrée ainsi que leurs requêtes REST correspondantes pour les inclure dans le contexte. Plutôt que d'utiliser des requêtes aléatoires dans ce contexte, cette méthode consiste à enrichir le contexte avec des requêtes REST similaires à la question d'entrée. Cela permet au modèle de générer des requêtes qui sont à la fois syntaxiquement correctes et contextuellement pertinentes.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/notebooks/REST_Request.ipynb)

### --- Explication des codes pour REST ---
Le dossier REST_Methods contient:

Les méthodes utilisées pour générer des requêtes REST à partir de questions en langage naturel, nous avons travaillé sur In_Context_learning: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/REST_Methods/In_Context_Learning_REST.py), RAG: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/REST_Methods/RAG_REST.py) et Agent: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/REST_Methods/Agent_REST.py)

Le fichier rag__DATA.xlsx : contient des exemples de questions en langage naturel ainsi que leurs équivalents en requêtes REST, afin d'enrichir le contexte dans la méthode RAG et Agent. 

Context_REST : [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/REST_Methods/Context_REST.py) est un fichier qui contient le contexte à transmettre au prompt pour chaque méthode.

Queries_Rest.xlsx : représente l'ensemble des questions en langage naturel utilisées pour les tests.

Pour faire fonctionner, par exemple, la méthode RAG, il faut d'abord exécuter le fichier Context_REST pour obtenir le contexte, puis exécuter le fichier RAG { Dans les scripts des méthodes, il est nécessaire de choisir le LLM à utiliser. Nous avons mentionné trois options au début du script, mais il faut sélectionner celle souhaitée avant d'exécuter le code }. L'exécution de ce dernier produit un fichier Excel contenant les questions en langage naturel en entrée ainsi que les requêtes correspondantes générées par le modèle.
Pour évaluer ces requêtes, il est nécessaire de charger ce fichier dans la liste des modèles au début du script d'évaluation REST:  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/landmatrix_evaluation_lib/Evaluation_REST.py) qui renverra ensuite les métriques d'évaluation.

**Reproduire les résultats** :

```bash
git clone https://github.com/tetis-nlp/landmatrix-graphql-python.git
```
- Installation de l'environnement python

```bash
conda create -n landmatrix python=3.9 pandas scikit-learn spacy
conda activate landmatrix
conda install -c conda-forge sentence-transformers
pip install transformers faiss-cpu
pip install ollama
pip install langchain-openai
pip install langchain-community
pip install openpyxl

- Téléchargement du modèle Spacy

```bash
python -m spacy download en_core_web_sm
```

- Installation et lancement de ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
ollama pull llama3:8b
```

- Configurer les clés API
```bash
cp credentials.ini.default credentials.ini
vim credentials.ini
```
add your own ISDM API keys

- Lancement de la méthode
```bash
python src/experiments.py 
```

