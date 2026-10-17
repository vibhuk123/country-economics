import streamlit as st
import plotly as px
from api import get_indicator, format_indicator, INDICATORS

st.title('Comparing Countries')
st.write('Compare economic indicators across two countries')

col1, col2 = st.columns(2)

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

with col1:
    country1 = st.selectbox('First country', list(countries.keys()), index=0)

with col2:
    country2 = st.selectbox('Second country', list(countries.keys()), index=1)

country_code1 = countries[country1]
country_code2 = countries[country2]

st.header(f'{country1} VS {country2}')

for name, indicator_code in INDICATORS.items():
    data1 = get_indicator(country_code1, indicator_code)
    data2 = get_indicator(country_code2, indicator_code)

    st.subheader(name)

    col1, col2 = st.columns(2)

    with col1:
        if not data1.empty:
            latest1 = data1.iloc[0]
            st.metric(country1, format_indicator(name, latest1['value']), help=f'Latest available year: {int(latest1['year'])}')
        else:
            st.metric(country1, 'No data available')

    with col2:
        if not data2.empty:
            latest2 = data2.iloc[0]
            st.metric(country2, format_indicator(name, latest2['value']), help=f'Latest available year: {int(latest2['year'])}')
        else:
            st.metric(country2, 'No data available')


st.page_link('app.py', label='Return to dashboard', icon='🏠')