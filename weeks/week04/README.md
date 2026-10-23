# Week 4: Data · APIs and scrapers

**Lecture practical:** Scraping your own website with BeautifulSoup
**Seminar:** APIs, and building a **live chart** with the World Bank API

## Notebooks

Click **Open in Colab**, then **File → Save a copy in Drive** before you start.

| # | Notebook | Open | When | What it covers |
|---|---|---|---|---|
| 1 | [`DS4_1_Scraping`](notebooks/DS4_1_Scraping.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week04/notebooks/DS4_1_Scraping.ipynb) | **Core**: lecture practical | Scraping your own website with BeautifulSoup |
| 2 | [`DS4_2_API_WorldBank`](notebooks/DS4_2_API_WorldBank.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week04/notebooks/DS4_2_API_WorldBank.ipynb) | **Core**: seminar | The World Bank API in Python: `requests`, JSON, `json_normalize`, and the `wbgapi` package |
| 3 | [`DS4_3_BeautifulSoup_Intro`](notebooks/DS4_3_BeautifulSoup_Intro.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week04/notebooks/DS4_3_BeautifulSoup_Intro.ipynb) | Practice | BeautifulSoup step by step: finding elements, classes, ids, with exercises |
| 4 | [`DS4_4_Scraping_HTML_Tables`](notebooks/DS4_4_Scraping_HTML_Tables.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week04/notebooks/DS4_4_Scraping_HTML_Tables.ipynb) | Practice | Reading tables from a web page with `pd.read_html` (Wikipedia G7 summits) |
| 5 | [`DS4_5_Scraping_Articles`](notebooks/DS4_5_Scraping_Articles.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week04/notebooks/DS4_5_Scraping_Articles.ipynb) | Stretch | Scraping an article's text and making a word cloud |
| 6 | [`DS4_6_Scraping_PDFs`](notebooks/DS4_6_Scraping_PDFs.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week04/notebooks/DS4_6_Scraping_PDFs.ipynb) | Stretch | Extracting tables from a PDF with `camelot` |
| 7 | [`DS4_7_API_CarbonIntensity`](notebooks/DS4_7_API_CarbonIntensity.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week04/notebooks/DS4_7_API_CarbonIntensity.ipynb) | Stretch | A live UK electricity API: re-run to get the latest forecast |

## Live chart examples (Vega-Lite)

These charts load their data **straight from an API** each time the page opens, so they stay up to date by themselves. Copy one into the [Vega-Lite editor](https://vega.github.io/editor/) to try it.

| Chart | What's new |
|---|---|
| [`worldbank_chart1_basic.json`](examples/worldbank_chart1_basic.json) | The API URL as the data source. `"property": "[1]"` picks the data out of the response; `per_page=100` gets every year |
| [`worldbank_chart2_replacement_rate.json`](examples/worldbank_chart2_replacement_rate.json) | Styling, plus a layered reference line at the replacement rate (2.1) |
| [`worldbank_chart3_multiline.json`](examples/worldbank_chart3_multiline.json) | Several groups in one request (`lic;lmc;mic;umc;hic`), coloured by `country.value` (nested JSON) |
| [`worldbank_chart4_multiline_styled.json`](examples/worldbank_chart4_multiline_styled.json) | Custom colours and axis title placement |
| [`worldbank_chart5_direct_labels.json`](examples/worldbank_chart5_direct_labels.json) | Labels at the end of each line instead of a legend |
| [`police_crime_bristol.json`](examples/police_crime_bristol.json) | A different API: street crime near a location, counted by type |
| [`frankfurter_gbp_daily.json`](examples/frankfurter_gbp_daily.json) | **Daily** data: exchange rates for £1, updated every working day. The response is a simple list, so no `"property"` is needed |

## API tips

- **Open the URL in your browser first.** If you can see data there, your chart or code can use it.
- **Check the metadata.** The World Bank sends 50 rows by default: add `per_page=100` (or more).
- **The latest year is often empty.** Filter out missing values: `"transform": [{"filter": "datum.value != null"}]`.
- **Never put an API key in a public chart or repository.** Anything on your website can be read by anyone.

## Data

- [`data/elizabeth-line-evaluation_excerpt.pdf`](data/elizabeth-line-evaluation_excerpt.pdf): used in `DS4_6_Scraping_PDFs`

## Portfolio

**CC5 (API task):** add a chart that uses a live API as its data source, with a short description of the API below it: the base URL, the parameters you used, and your full URL.
