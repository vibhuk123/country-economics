import streamlit as st
import plotly.express as px
from api import get_indicator, format_indicator, INDICATORS
import pandas as pd

st.title('Comparing Countries')
st.write('Compare economic indicators across two countries')

st.page_link('app.py', label='Return to dashboard', icon='🏠')

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

# Compare GDP Growth
st.header('GDP Growth Comparison')

growth1 = get_indicator(country_code1, INDICATORS['GDP growth'])
growth2 = get_indicator(country_code2, INDICATORS['GDP growth'])

if not growth1.empty and not growth2.empty:
    growth1 = growth1.sort_values('year')
    growth2 = growth2.sort_values('year')

    growth1['Country'] = country1
    growth2['Country'] = country2

    combined_growth = pd.concat([growth1, growth2], ignore_index=True)

    growth_line_chart = px.line(
        combined_growth,
        x='year',
        y='value',
        color='Country',
        title=f'Annual GDP growth (%)',
        labels={
            'year': 'Year',
            'value': 'GDP Growth (%)',
            'Country': 'Country'
        }
    )

    growth_line_chart.update_layout(hovermode='x unified', yaxis_tickformat='.2f', yaxis_ticksuffix='%')

    st.plotly_chart(growth_line_chart, use_container_width=True)
else:
    st.warning('GDP growth data unavaiable')

# Compare GDP Per Capita 
st.header('GDP Per Capita Comparison')

percapita1 = get_indicator(country_code1, INDICATORS['GDP per capita'])
percapita2 = get_indicator(country_code2, INDICATORS['GDP per capita'])

if not percapita1.empty and not percapita2.empty:
    percapita1 = percapita1.sort_values('year')
    percapita2 = percapita2.sort_values('year')

    percapita1['Country'] = country1
    percapita2['Country'] = country2

    combined_per_capita = pd.concat([percapita1, percapita2], ignore_index=True)

    per_capita_line_chart = px.line(
        combined_per_capita,
        x='year',
        y='value',
        color='Country',
        title=f'Annual GDP Per Capita ($)',
        labels={
            'year': 'Year',
            'value': 'GDP Per Capita ($)',
            'Country': 'Country'
        }
    )

    per_capita_line_chart.update_layout(hovermode='x unified', yaxis_tickformat='$,.2f')

    st.plotly_chart(per_capita_line_chart, use_container_width=True)
else:
    st.warning('GDP Per Capita data unavailable')

# Compare inflation
st.header('Inflation Comparison')

inflation1 = get_indicator(country_code1, INDICATORS['Inflation'])
inflation2 = get_indicator(country_code2, INDICATORS['Inflation'])

if not inflation1.empty and not inflation2.empty:
    inflation1 = inflation1.sort_values('year')
    inflation2 = inflation2.sort_values('year')

    inflation1['Country'] = country1
    inflation2['Country'] = country2

    combined_inflation = pd.concat([inflation1, inflation2], ignore_index=True)

    inflation_line_chart = px.line(
        combined_inflation,
        x='year',
        y='value',
        color='Country',
        title=f'Annual Inflation Rate (%)',
        labels={
            'year': 'Year',
            'value': 'Inflation Rate (%)',
            'Country': 'Country'
        }
    )

    inflation_line_chart.update_layout(hovermode='x unified', yaxis_ticksuffix='%')

    st.plotly_chart(inflation_line_chart, use_container_width=True)
else:
    st.warning('Inflation data unavailable')