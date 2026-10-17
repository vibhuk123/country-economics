import streamlit as st
import plotly.express as px

from api import get_indicator, INDICATORS, format_indicator

st.set_page_config(page_title='Country Economics Dashboard', page_icon='🌍', layout='wide')

st.title('Country Economics Dashboard')
st.write('Explore economic indicators across the globe')

countries = {
    'India': 'IND',
    'United States': 'USA',
    'United Kingdom': 'GBR',
    'Germany': 'DEU',
    'China': 'CHN',
    'Japan': 'JPN',
    'Brazil': 'BRA',
    'Canada': 'CAN',
    'Australia': 'AUS',
}

country = st.selectbox('Select a country', list(countries.keys()))
country_code = countries[country]

st.header(f'{country} Economic Overview')