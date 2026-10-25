# Country Economics Dashboard

An interactive dashboard for exploring and comparing economic indicators across countries using data from the [World Bank Open Data API](https://data.worldbank.org/).

Built with Python, Streamlit, Pandas, and Plotly, this project makes international economic data easier to explore through interactive visualizations, side-by-side comparisons, and downloadable datasets.

## Features

### Country Dashboard
- Explore economic indicators for individual countries.
- View the latest available data for each indicator.
- Visualize economic trends over time using interactive charts.

### Country Comparison
- Compare two countries side by side.
- Select a custom year range to explore historical trends.
- View comparisons of GDP growth, GDP per capita, real GDP per capita, and inflation.
- Examine summary statistics, including average GDP growth, average inflation, and changes in GDP per capita over the selected period.

### Data Export
- Download economic data for both selected countries as a CSV file.
- Export data across multiple indicators and years for further analysis.

### Data Source
- Retrieve economic data from the World Bank API.
- Handle missing observations and differences in data availability across countries and indicators.
- Cache API responses to reduce unnecessary requests and improve performance.

## Economic Indicators

The dashboard includes the following indicators:

| Indicator | Description |
|---|---|
| GDP | Gross domestic product in current US dollars |
| GDP per capita | GDP per person in current US dollars |
| Real GDP per capita | GDP per person in constant 2015 US dollars |
| GDP growth | Annual percentage growth in GDP |
| Inflation | Annual consumer price inflation rate |
| Unemployment | Unemployment as a percentage of the labor force |
| Population | Total population |

Data availability varies by country, indicator, and year. The dashboard uses the latest available observations where appropriate.

## Technology Stack

- **Python** — application logic and data processing
- **Streamlit** — interactive web application
- **Pandas** — data manipulation and analysis
- **Plotly Express** — interactive charts
- **Requests** — World Bank API requests
- **World Bank Open Data API** — economic data source

## Project Structure

```text
country-economics/
├── app.py                  # Main country dashboard
├── api.py                  # API requests and data formatting
├── indicators.py           # Economic indicator definitions
├── charts.py               # Chart-related functionality
├── analysis.py             # Economic analysis
├── pages/
│   └── compare_countries.py  # Country comparison page
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Git
- An internet connection to retrieve data from the World Bank API

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vibhuk123/country-economics.git
   cd country-economics
   ```

2. Create and activate a virtual environment:

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the dashboard:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL displayed in your terminal, usually `http://localhost:8501`.

No World Bank API key is required.

## Data and Methodology

Economic data is retrieved from the World Bank's public API. Indicators use different units and measurement conventions, so values are formatted according to the indicator being displayed.

- **GDP and GDP per capita** use current US dollars, meaning values can change due to inflation and exchange-rate movements as well as changes in economic output.
- **Real GDP per capita** uses constant 2015 US dollars to help examine changes over time after accounting for price-level changes.
- **GDP growth and inflation** are reported as annual percentages.
- **Country comparisons** use common years when calculating statistics that require observations from both countries.

The latest available year may differ between indicators and countries. Historical comparisons are therefore limited by the observations available from the data source.

## Future Improvements

Potential areas for further development include:

- Expanding the selection of countries and economic indicators.
- Adding additional visualizations and comparative economic statistics.
- Improving the presentation of missing data and differences in reporting periods.
- Deploying the dashboard online for public access.

## Acknowledgments

- [World Bank Open Data](https://data.worldbank.org/) for providing publicly accessible economic data.
- [Streamlit](https://streamlit.io/) for the application framework.
- [Plotly](https://plotly.com/python/) for interactive data visualization.
