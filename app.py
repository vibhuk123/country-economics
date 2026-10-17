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

for name, code in INDICATORS.items():
    data = get_indicator(country_code, code)

    if not data.empty:
        latest = data.iloc[0]
        formatted_value = format_indicator(name, latest['value'])
        st.metric(name, formatted_value, help=f'Latest available year: {int(latest['year'])}')
    else:
        st.metric(name, 'No data available!')

st.header('GDP over time')

gdp = get_indicator(country_code, INDICATORS['GDP'])

if not gdp.empty:
    gdp = gdp.sort_values('year')

    line_chart = px.line(
        gdp,
        x='year',
        y='value',
        title=f'{country} GDP (US$)',
        labels={
            'year': 'Year',
            'value': 'GDP (US$)'
        }
    )

    line_chart.update_layout(
        hovermode='x unified',
        yaxis_tickformat='$,.3s'
    )

    st.plotly_chart(line_chart, use_container_width=True)

else:
    st.warning(f'GDP data is not available for country: {country}')