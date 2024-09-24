# Help with querying the *Land Matrix* database via Python
[![Land Matrix](https://landmatrix.org/images/lm-logo-dark.png)](https://landmatrix.org/)

This project aims to facilitate the retrieval of Land Matrix data through natural language queries.

This repository provides several resources:
- An end-to-end **Streamlit** application with optimal configuration. [Explanations.](streamlit_chatbot_landmatrix/README.md)
- A **pipeline to reproduce** our benchmark of models and methods. [See below](#2-reproduce-our-benchmark)
- **Educational notebooks** that describe all the tasks needed for the entire pipeline. [Explanations.](notebooks/README.md)

## 1. Installation
```bash
git clone https://github.com/tetis-nlp/landmatrix-graphql-python.git
```
- Installation of the Python environment

    ```bash
    conda create -n landmatrix python=3.9 pandas scikit-learn spacy
    conda activate landmatrix
    conda install -c conda-forge sentence-transformers
    pip install transformers faiss-cpu
    pip install ollama
    pip install langchain-openai
    pip install langchain-community
    pip install openpyxl
    ```

- Downloading the Spacy model

    ```bash
    python -m spacy download en_core_web_sm
    ```

- Installation and launch of Ollama
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ollama serve
    ollama pull llama3:8b
    ```

- Configure API keys (only compatible with [chat ISDM](https://isdm-chat.crocc.meso.umontpellier.fr/))
    ```bash
    cp credentials.ini.default credentials.ini
    vim credentials.ini
    ```
add your own ISDM API keys


## 2. Reproduce our benchmark

    ```bash
    python src/experiments.py 
    ```

- *Monitore your pipeline* : `tail -f logs/pipeline.log`
- *Stop the pipeline: Kill all the subprocess*: `pkill -f src/`







