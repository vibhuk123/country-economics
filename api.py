import requests
import pandas as pd
import streamlit as st

INDICATORS = {
    "GDP": "NY.GDP.MKTP.CD",
    "GDP per capita": "NY.GDP.PCAP.CD",
    "GDP growth": "NY.GDP.MKTP.KD.ZG",
    "Inflation": "FP.CPI.TOTL.ZG",
    "Unemployment": "SL.UEM.TOTL.ZS",
    "Population": "SP.POP.TOTL"
}

@st.cache_data(ttl=3600)
def get_indicator(country, indicator):
    # get historical economic data 

    url = (f'https://api.worldbank.org/v2/country/{country}/indicator/{indicator}')

    parameters = {
        'format': 'json',
        'date': '2000:2025',
        'per_page': 100
    }

    response = requests.get(url, params=parameters, timeout=15)
    response.raise_for_status()

    result = response.json()

    if not isinstance(result, list) or len(result) < 2:
        return pd.DataFrame(columns=['year', 'value'])

    records = result[1] or []

    data = [
        {
            'year': int(item['date']),
            'value': int(item['value'])
        }
        for item in records if item ['value'] is not None
    ]

    return pd.DataFrame(data).sort_values('year', ascending=False)

def format_indicator(name, value):
    if name == 'GDP':
        return f'${value / 1_000_000_000_000:.2f} trillion'

    elif name == 'GDP per capita':
        return f'${value:,.0f}'

    elif name in ['GDP growth', 'Inflation', 'Unemployment']:
        return f'{value:.2f}%'

    elif name == 'Population':
        return f'{value:,.0f}'

    return f'{value:,.2f}'

if __name__ == '__main__':
    for name, code in INDICATORS.items():
        data = get_indicator("IND", code)

        if not data.empty:
            latest = data.iloc[0]
            formatted_value = format_indicator(name, latest['value'])
            print(f'{name}: {formatted_value} ({int(latest['year'])})')
        else:
            print(f'{name}: no data available')