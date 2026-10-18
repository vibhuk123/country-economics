import streamlit as st
import plotly.express as px

from api import get_indicator, INDICATORS, format_indicator

st.set_page_config(page_title='Country Economics Dashboard', page_icon='🌍', layout='wide', initial_sidebar_state='collapsed')

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

# GDP Over Time
st.header('GDP Over Time')

gdp = get_indicator(country_code, INDICATORS['GDP'])

if not gdp.empty:
    gdp = gdp.sort_values('year')

    gdp_line_chart = px.line(
        gdp,
        x='year',
        y='value',
        title=f'{country} GDP ($)',
        labels={
            'year': 'Year',
            'value': 'GDP ($)'
        }
    )

    gdp_line_chart.update_layout(hovermode='x unified', yaxis_tickformat='$,.3s')

    st.plotly_chart(gdp_line_chart, width='stretch')
else:
    st.warning(f'GDP data is not available for {country}')

# GDP Growth Over Time
st.header('GDP Growth Over Time')

gdp_growth = get_indicator(country_code, INDICATORS['GDP growth'])

if not gdp_growth.empty:
    gdp_growth = gdp_growth.sort_values('year')

    gdp_growth_line_chart = px.line(
        gdp_growth,
        x='year',
        y='value',
        title=f'{country} Annual GDP Growth',
        labels={
            'year': 'Year',
            'value': 'GDP Growth (%)'
        }
    )

    gdp_growth_line_chart.update_layout(hovermode='x unified', yaxis_ticksuffix='%')

    st.plotly_chart(gdp_growth_line_chart, width='stretch')
else:
    st.warning(f'GDP growth data is not available for {country}')

# Inflation Over Time
st.header('Inflation Over Time')

inflation = get_indicator(country_code, INDICATORS['Inflation'])

if not inflation.empty:
    inflation = inflation.sort_values('year')

    inflation_line_chart = px.line(
        inflation,
        x='year',
        y='value',
        title=f'{country} Annual Inflation Rate (%)',
        labels={
            'year': 'Year',
            'value': 'Inflation rate (%)'
        }
    )

    inflation_line_chart.update_layout(hovermode='x unified', yaxis_ticksuffix='%')

    st.plotly_chart(inflation_line_chart, width='stretch')
else:
    st.warning(f'Inflation data is not available for {country}')

# Unemployment Over Time
st.header('Unemployment Over Time')

unemployment = get_indicator(country_code, INDICATORS['Unemployment'])

if not unemployment.empty:
    unemployment = unemployment.sort_values('year')

    unemployment_line_chart = px.line(
        unemployment,
        x='year',
        y='value',
        title=f'{country} Annual Unemployment Rate (%)',
        labels={
            'year': 'Year',
            'value': 'Unemployment rate (%)'
        }
    )

    unemployment_line_chart.update_layout(hovermode='x unified', yaxis_ticksuffix='%')

    st.plotly_chart(unemployment_line_chart, width='stretch')
else:
    st.warning(f'Unemployment data not available for {country}')

# Population Over Time
st.header('Population Over Time')

population = get_indicator(country_code, INDICATORS['Population'])

if not population.empty:
    population = population.sort_values('year')

    population_line_chart = px.line(
        population,
        x='year',
        y='value',
        title=f'{country} Population',
        labels={
            'year': 'Year',
            'value': 'Population'
        }
    )

    population_line_chart.update_layout(hovermode='x unified', yaxis_tickformat=',.0f')

    st.plotly_chart(population_line_chart, width='stretch')
else:
    st.warning(f'Population data not available for {country}')

st.page_link('pages/compare_countries.py', label='Compare Countries', icon='📊')