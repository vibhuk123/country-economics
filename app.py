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

# Display values
for name, code in INDICATORS.items():
        data = get_indicator(country_code, code)

        if not data.empty:
            latest = data.iloc[0]
            formatted_value = format_indicator(name, latest['value'])
            st.metric(name, formatted_value, help = f'Latest available year: {int(latest['year'])}')
        else:
            st.metric(name, 'No data!')