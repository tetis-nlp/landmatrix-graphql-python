from langchain_core.output_parsers import StrOutputParser
import pandas as pd
import json
import BD_Value
import streamlit as st  
import plotly.express as px  
import Global_Code_LMI
from langchain_community.llms import Ollama


# Define variables used for processing
#-----------------------------------

parser = StrOutputParser()
countries = BD_Value.countries
context = BD_Value.context
data = json.loads(context)
country_dict = {country['id']: country['country.name'] for country in countries}


###################### API submition #############################

# Function to display the modal popup
def show_modal():
    st.markdown(
        """
        <style>
        /* The Modal (background) */
        .modal {
          display: block; /* Show the modal by default */
          position: fixed;
          z-index: 1; /* Sit on top */
          left: 0;
          top: 0;
          width: 100%; /* Full width */
          height: 100%; /* Full height */
          background-color: rgba(0, 0, 0, 0.5); /* Black w/ opacity */
        }

        /* Modal Content/Box */
        .modal-content {
          background-color: #fefefe;
          margin: 15% auto; /* 15% from the top and centered */
          padding: 20px;
          border: 1px solid #888;
          width: 300px; /* Could be more or less, depending on screen size */
          border-radius: 10px;
          box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
        }

        /* The Close Button */
        .close {
          color: #aaa;
          float: right;
          font-size: 28px;
          font-weight: bold;
        }

        .close:hover,
        .close:focus {
          color: black;
          text-decoration: none;
          cursor: pointer;
        }
        </style>

        <div id="myModal" class="modal">
          <div class="modal-content">
            <span class="close" onclick="document.getElementById('myModal').style.display='none'">&times;</span>
            <h2>Enter your API Key</h2>
            <form>
              <input type="text" id="apiKeyInput" name="api_key" style="width:100%;padding:8px;margin-bottom:10px;" placeholder="Enter API key here..."><br>
              <button onclick="storeApiKey()" style="padding:10px;width:100%;">Submit</button>
            </form>
          </div>
        </div>

        <script>
        function storeApiKey() {
          var apiKey = document.getElementById('apiKeyInput').value;
          // Store API key in localStorage
          localStorage.setItem('api_key', apiKey);
          // Close the modal and reload the page
          document.getElementById('myModal').style.display = 'none';
          window.location.reload();
        }

        window.onload = function() {
          // If API key is in localStorage, pass it to Streamlit via hidden input
          const apiKey = localStorage.getItem('api_key');
          if (apiKey) {
            const apiKeyInput = document.createElement("input");
            apiKeyInput.type = "hidden";
            apiKeyInput.name = "api_key";
            apiKeyInput.value = apiKey;
            document.body.appendChild(apiKeyInput);
            
            const form = document.createElement("form");
            form.method = "POST";
            form.appendChild(apiKeyInput);
            document.body.appendChild(form);
            form.submit();
          }
        }
        </script>
        """,
        unsafe_allow_html=True
    )

# Check if the API key is present in session or query parameters
if 'api_key' not in st.session_state:
    # Use the new `st.query_params()` instead of deprecated `st.experimental_get_query_params()`
    query_params = st.query_params  # Get query parameters

    # Check if 'api_key' is in the query params
    if 'api_key' in query_params:
        st.session_state['api_key'] = query_params['api_key']  # Save the API key to session state
        st.rerun()  # Use `st.rerun()` instead of `st.experimental_rerun()`

# Show main content if the API key is stored
if 'api_key' in st.session_state:

    api_key = st.session_state['api_key']  # Récupère la clé API de la session
    llm = Global_Code_LMI.llm(api_key)  # Initialiser l'instance LLM avec la clé API

    # Check if 'df' is not already in the session state
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame()  # Initialize an empty DataFrame
    
    # Continue with the rest of your application logic
    st.title(' :orange[LAND MATRIX] _ChatBot_ :earth_africa:')
    
    question = st.text_input("Enter your question...")

    if st.button("Generate", type="primary"):
        URL = Global_Code_LMI.ChatBot_response(llm, parser, question)

        # While loop for handling empty URLs
        counter = 0
        max_attempts = 15
        while URL is None and counter < max_attempts:
            URL = Global_Code_LMI.ChatBot_response(llm, parser, question)
            counter += 1

        if URL is None:
            st.warning('Rephrase your response or provide more details...', icon="⚠️")
        else:
            st.write(URL)
            separated_urls = Global_Code_LMI.split_country_ids(URL)
            headers = {'accept': 'application/json'}
            combined_data = Global_Code_LMI.fetch_data_from_urls(separated_urls, headers)
            st.session_state.df = Global_Code_LMI.Mapping_groups(combined_data, country_dict)

    df = st.session_state.df

    # Data exploration when receiving data
    if not df.empty:
        if df['fully_updated_at'] is not None:
            df['year'] = df['fully_updated_at'].str.extract(r'(\d{4})')
        else:
            df['year'] = None

        # Visualizations
        tab1, tab2, tab3, tab4 = st.tabs(["Data", "Countries Visualization", "Investment by year", "Intention of investment"])

        with tab1:
            st.header("Data")
            st.dataframe(df)

        with tab2:
            st.header("Countries_Visualization")
            # Group and count deals by country
            df_grouped = df.groupby('country_name').id.count().reset_index()
            df_grouped.columns = ['Name of Countries', 'Number of deals']
            
            # Sort countries by number of deals
            df_grouped = df_grouped.sort_values(by='Number of deals', ascending=False)
            
            # Create a horizontal bar chart
            fig = px.bar(
                df_grouped,
                x='Number of deals',
                y='Name of Countries',
                orientation='h',  # Horizontal bar chart
                color_discrete_sequence=['green'],
                template='plotly_white',
                title='<b>Sum of IDs by Country ID</b>'
            )
            st.plotly_chart(fig)

        with tab3:
            st.header("Year_Visualization")
            # Group and count deals by year
            df_grouped2 = df.groupby('year').id.count().reset_index()
            df_grouped2.columns = ['year', 'Number of deals']
            
            fig = px.bar(
                df_grouped2,
                x='year',
                y='Number of deals',
                orientation='v',  # Vertical bar chart
                color_discrete_sequence=['green'],
                template='plotly_white',
                title='<b>Investments by year "Bar Chart"</b>'
            )
            st.plotly_chart(fig)
            
            # Create the line chart using Plotly
            fig = px.line(df_grouped2, x='year', y='Number of deals', title='Investments by Year "Line Chart"')
            st.plotly_chart(fig)

        with tab4:
            st.header(" Intention of investment ")

            # Explode the 'group' column to obtain each individual group
            df_exploded = df.assign(group=df['group'].str.split(', ')).explode('group')

            # Group by 'group' and count occurrences
            df_grouped_by_group = df_exploded.groupby('group').id.count().reset_index()
            df_grouped_by_group.columns = ['Group', 'Number of deals']

            # Sort by number of occurrences in ascending order
            df_grouped_by_group = df_grouped_by_group.sort_values(by='Number of deals', ascending=True)

            # Create a horizontal bar chart 
            fig_group = px.bar(df_grouped_by_group, x='Number of deals', y='Group', orientation='h', 
                    color_discrete_sequence=['green'], template='plotly_white', title='<b>Deals by Group "Bar Chart"</b>')
            fig_group.update_layout(
                height=600,  # Adjust the height as needed
                width=1000   # Adjust the width as needed
            )
            st.plotly_chart(fig_group)

    else:
        st.write("")

else:
    show_modal()