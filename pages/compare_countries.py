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

start_year, end_year = st.slider(
    label='Select year range',
    min_value=2000,
    max_value=2025,
    value=(2000,2025),
    step=1
)

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

growth1 = growth1[growth1['year'].between(start_year, end_year)]
growth2 = growth2[growth2['year'].between(start_year, end_year)]

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

    st.plotly_chart(growth_line_chart, width='stretch')
else:
    st.warning('GDP growth data unavaiable')

# Compare GDP Per Capita 
st.header('GDP Per Capita Comparison')

percapita1 = get_indicator(country_code1, INDICATORS['GDP per capita'])
percapita2 = get_indicator(country_code2, INDICATORS['GDP per capita'])

percapita1 = percapita1[percapita1['year'].between(start_year, end_year)]
percapita2 = percapita2[percapita2['year'].between(start_year, end_year)]

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

    st.plotly_chart(per_capita_line_chart, width='stretch')
else:
    st.warning('GDP Per Capita data unavailable')

# Compare Real GDP Per Capita Data
st.header('Real GDP Per Capita Comparison')

real_gdp1 = get_indicator(country_code1, INDICATORS['Real GDP per capita'])
real_gdp2 = get_indicator(country_code2, INDICATORS['Real GDP per capita'])

real_gdp1 = real_gdp1[real_gdp1['year'].between(start_year, end_year)]
real_gdp2 = real_gdp2[real_gdp2['year'].between(start_year, end_year)]

if not real_gdp1.empty and not real_gdp2.empty:
    real_gdp1 = real_gdp1.sort_values('year').copy()
    real_gdp2 = real_gdp2.sort_values('year').copy()

    real_gdp1['Country'] = country1
    real_gdp2['Country'] = country2

    combined_real_gdp = pd.concat([real_gdp1, real_gdp2], ignore_index=True)

    real_gdp_line_chart = px.line(
        combined_real_gdp,
        x='year',
        y='value',
        color='Country',
        title='GDP Per Capita (Constant 2015 $)',
        labels={
            'year': 'Year',
            'value': 'Real GDP Per Capita (2015 $)',
            'Country': 'Country'
        }
    )

    real_gdp_line_chart.update_layout(hovermode='x unified', yaxis_tickformat='$,.0f')

    st.plotly_chart(real_gdp_line_chart, width='stretch')
else:
    st.warning('Data not available')

# Compare inflation
st.header('Inflation Comparison')

inflation1 = get_indicator(country_code1, INDICATORS['Inflation'])
inflation2 = get_indicator(country_code2, INDICATORS['Inflation'])

inflation1 = inflation1[inflation1['year'].between(start_year, end_year)]
inflation2 = inflation2[inflation2['year'].between(start_year, end_year)]

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

    st.plotly_chart(inflation_line_chart, width='stretch')
else:
    st.warning('Inflation data unavailable')

# Economic Insights
st.header('Economic Insights')
st.write(f'Economic comparisons for {country1} and {country2} from {start_year} to {end_year}')

def compare_common_years(data1, data2):
    convert1 = data1[['year', 'value']].rename(columns={'value': 'value1'})
    convert2 = data2[['year', 'value']].rename(columns={'value': 'value2'})

    return (pd.merge(convert1, convert2, on='year', how='inner').sort_values('year'))

# Average GDP Growth
st.subheader('Average GDP Growth')

common_gdp_growth = compare_common_years(growth1, growth2)

if not common_gdp_growth.empty:
    avg_gdp_growth_1 = common_gdp_growth['value1'].mean()
    avg_gdp_growth_2 = common_gdp_growth['value2'].mean()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label=f'{country1} average', value=f'{avg_gdp_growth_1:.2f}%')
    with col2:
        st.metric(label=f'{country2} average', value=f'{avg_gdp_growth_2:.2f}%')
else:
    st.warning('No data available!')

# GDP Per Capita 
st.subheader('GDP Per Capita Change')

common_gdp_per_capita = compare_common_years(percapita1, percapita2)

if len(common_gdp_per_capita) >= 2:
    first_year = common_gdp_per_capita.iloc[0]
    last_year = common_gdp_per_capita.iloc[-1]

    start1 = first_year['value1']
    end1 = last_year['value1']
    start2 = first_year['value2']
    end2 = last_year['value2']

    if start1 > 0 and start2 > 0:
        change1 = ((end1/start1)-1)*100
        change2 = ((end2/start2)-1)*100

        st.caption(f'Change from {int(first_year['year'])} to {int(last_year['year'])}')

        col1, col2 = st.columns(2)

        with col1:
            st.metric(label=f'{country1} change', value=f'{change1:+.2f}%')           
        with col2:
           st.metric(label=f'{country2} change', value=f'{change2:+.2f}%')
    else:
        st.warning('Data not available')
else:
    st.warning('Data not available')

# Average inflation 
st.subheader('Average Annual Inflation')

common_inflation = compare_common_years(inflation1, inflation2)

if not common_inflation.empty:
    avg_inflation1 = common_inflation['value1'].mean()
    avg_inflation2 = common_inflation['value2'].mean()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label=f'{country1} average', value=f'{avg_inflation1:.2f}%')
    with col2:
        st.metric(label=f'{country2} average', value=f'{avg_inflation2:.2f}%')
else:
    st.warning('Data not available')

# Download Data
st.header('Download Data')
st.write('Download economic data for further analysis')

download_data = []

indicators_to_download = {
    'GDP': INDICATORS['GDP'],
    'GDP per capita': INDICATORS['GDP per capita'],
    'GDP growth': INDICATORS['GDP growth'],
    'Inflation': INDICATORS['Inflation'],
    'Unemployment': INDICATORS['Unemployment'],
    'Population': INDICATORS['Population'],
}

for indicator_name, indicator_code in indicators_to_download.items():
    data1 = get_indicator(country_code1, indicator_code)
    data2 = get_indicator(country_code2, indicator_code)

    data1 = data1[data1['year'].between(start_year, end_year)]
    data2 = data2[data2['year'].between(start_year, end_year)]

    for _, row in data1.iterrows():
        download_data.append({
            'Country': country1,
            'Year': int(row['year']),
            'Indicator': indicator_name,
            'Value': row['value']
        })

    for _, row in data2.iterrows():
        download_data.append({
            'Country': country2,
            'Year': int(row['year']),
            'Indicator': indicator_name,
            'Value': row['value']
        })

download_df = pd.DataFrame(download_data)

if not download_df.empty:
    data_csv = download_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label='Download Comparison Data (csv)',
        data=data_csv,
        file_name=f'{country1}_vs_{country2}_from_{start_year}_to_{end_year}.csv',
        mime='text/csv'
    )
else:
    st.warning('No data available')