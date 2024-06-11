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

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tetis-nlp/landmatrix-graphql-python/blob/main/Corresponding_Similarity.ipynb)

