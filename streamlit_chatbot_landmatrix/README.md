# Streamlit application

First, you need to get your [chat ISDM](https://isdm-chat.crocc.meso.umontpellier.fr/) API Key. You'll need a e-mail address from a reseach organism located in Montpellier.
ISDM is a service from the University of Montpellier which provides API to two LLM : Codestral-22B and Mixtral-8x7B (47B).
For this application, we use Codestral-22B.

## Using through the free streamlit cloud service
The application can be tested through the free streamlit cloud service (but latence is not great): [link to streamlite cloud](https://appchatbotlandmatrix-gxkez3drqxdznyvczq5wtg.streamlit.app/)

## Start the application in standalone 
- Installation
    ```bash
    pip install streamlit
    ```
- Run the app
    ```bash
    streamlit run streamlit_chatbot_landmatrix/page_finale.py
    ```
