from langchain_core.output_parsers import StrOutputParser
import pandas as pd
import json
import BD_Value
import streamlit as st  
import plotly.express as px  
import Global_Code
from langchain_community.llms import Ollama


# Define variables used for processing
#-----------------------------------
llm = Global_Code.llm
parser = StrOutputParser()
countries = Global_Code.countries
context = BD_Value.context
data = json.loads(context)
counter = 0
max_attempts = 50
country_dict = {country['id']: country['country.name'] for country in countries}

MODEL = "llama3:8b"
llm = Ollama(model=MODEL)


# Check if 'df' is not already in the session state
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()  # Initialize an empty DataFrame

# Start with Streamlit
#----------------------

st.title(' :orange[LAND MATRIX] _ChatBot_ :earth_africa:')
question = st.text_input("Enter your question...")

if st.button("Generate", type="primary"):
    
    URL = Global_Code.ChatBot_response(llm, parser, question)      
    # While loop for handling empty URLs
    while URL is None and counter < max_attempts:
        URL = Global_Code.ChatBot_response(llm, parser, question)
        counter += 1     
    print(counter)
    if URL is None:
            st.warning('Rephrase your response or provide more details...', icon="⚠️")
    else:
            st.write(URL)
            separated_urls = Global_Code.split_country_ids(URL)
            headers = {'accept': 'application/json'}
            combined_data = Global_Code.fetch_data_from_urls(separated_urls, headers)
            st.session_state.df = Global_Code.Mapping_groups(combined_data, country_dict) 

df = st.session_state.df

# Data exploration when receiving data
#----------------------------------------

if not df.empty:
    if df['fully_updated_at'] is not None:
        df['year'] = df['fully_updated_at'].str.extract(r'(\d{4})')
    else:
        df['year'] = None
            
    #Visualizations
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
            color='Number of deals',
            color_continuous_scale=['black', 'yellow', 'green'],
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
            color='Number of deals',
            color_continuous_scale=['black', 'yellow', 'green'],
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
        fig_group = px.bar(df_grouped_by_group, x='Number of deals', y='Group', orientation='h', color='Number of deals',
                color_continuous_scale=['yellow', 'green', 'black'], template='plotly_white', title='<b>Deals by Group "Bar Chart"</b>')
        fig_group.update_layout(
            height=600,  # Adjust the height as needed
            width=1000   # Adjust the width as needed
        )
        st.plotly_chart(fig_group)

else:
    st.write("")
