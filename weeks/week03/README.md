# Week 3: Visualisation principles · Introducing Python

**Lecture practical:** Getting and cleaning data with Python ("Is the stock market overvalued?" part 1)
**Seminar:** Charting with Altair, and embedding the chart on your site (part 2)

We use **Google Colab** for these notebooks. Click a notebook's **Open in Colab** button below, then **File → Save a copy in Drive** before you start. The notebooks load their data from links, so there's nothing else to download.

## Notebooks

Notebooks are numbered in the order we suggest working through them. **Core** notebooks are covered in class; the rest are for practice and stretch in your own time.

| # | Notebook | Open | When | What it covers |
|---|---|---|---|---|
| 1 | [`DS3_1_PythonQuickStart`](notebooks/DS3_1_PythonQuickStart.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_1_PythonQuickStart.ipynb) | **Core**: lecture practical | Running cells, variables, types, lists, dictionaries (= JSON), packages |
| 2 | [`DS3_2_Requests_Shiller`](notebooks/DS3_2_Requests_Shiller.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_2_Requests_Shiller.ipynb) | **Core**: lecture practical | `requests`, loading a CSV, a new column, missing data, dates, saving a CSV |
| 3 | [`DS3_3_Altair_Shiller`](notebooks/DS3_3_Altair_Shiller.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_3_Altair_Shiller.ipynb) | **Core**: seminar | A first Altair chart, styling, an average line, saving JSON for your website |
| 4 | [`DS3_4_PythonBasics`](notebooks/DS3_4_PythonBasics.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_4_PythonBasics.ipynb) | Practice | Python basics in more depth, with exercises ([solutions](notebooks/DS3_4_PythonBasics_Solutions.ipynb)) |
| 5 | [`DS3_5_AltairBasics`](notebooks/DS3_5_AltairBasics.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_5_AltairBasics.ipynb) | Practice | More Altair: building blocks, inline vs URL data, chart types |
| 6 | [`DS3_6_PandasBasics`](notebooks/DS3_6_PandasBasics.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_6_PandasBasics.ipynb) | Practice | Reading Excel files, reshaping data with pandas |
| 7 | [`DS3_7_PandasRequests`](notebooks/DS3_7_PandasRequests.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_7_PandasRequests.ipynb) | Practice | Fetching data from an API, merging and reshaping |
| 8 | [`DS3_8_ShillerExcelToCSV`](notebooks/DS3_8_ShillerExcelToCSV.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week03/notebooks/DS3_8_ShillerExcelToCSV.ipynb) | Stretch | Turning Shiller's original Excel file into the clean CSV used in the lecture |

## Example charts

Four Vega-Lite charts that build on the seminar chart, step by step. Open one on GitHub, copy the JSON into the [Vega-Lite editor](https://vega.github.io/editor/), and compare it with the one before.

| Chart | What's new |
|---|---|
| [`shiller_chart1_basic.json`](examples/shiller_chart1_basic.json) | The chart saved from `DS3_3_Altair_Shiller`: line colour, title and subtitle, no vertical grid lines |
| [`shiller_chart2_styled.json`](examples/shiller_chart2_styled.json) | More styling: font, softer title colours, dashed grid lines, no chart border or y-axis line |
| [`shiller_chart3_cape_since1950.json`](examples/shiller_chart3_cape_since1950.json) | A `filter` **transform** to show 1950 onwards, and the y-axis switched to `CAPE` |
| [`shiller_chart4_cape_average.json`](examples/shiller_chart4_cape_average.json) | A **layered** chart: a dashed `rule` at the average CAPE (an `aggregate`) on top of the line |

Charts 2–4 were written directly in Vega-Lite, so there's no Altair code for them. Translating one into Altair is a good stretch exercise.

## Data

| File | What it is |
|---|---|
| [`data/data_shiller.xls`](data/data_shiller.xls) | Robert Shiller's original data, from [shillerdata.com](https://shillerdata.com/) (downloaded October 2026) |
| [`data/data_shiller.csv`](data/data_shiller.csv) | Cleaned from the Excel file (by `DS3_8`). Used in the lecture practical |
| [`data/data_shiller_clean.csv`](data/data_shiller_clean.csv) | The full output of `DS3_2`: every column (including real prices and `CAPE`), plus `PE_ratio` and `Date_iso`. Good for trying other variables |
| [`data/data_shiller_pe.csv`](data/data_shiller_pe.csv) | The chart-ready output of `DS3_2`: just `Date_iso` and `PE_ratio`. Use it in the seminar if you need to catch up |

## Portfolio

Add your styled P/E chart (or a chart of your own data, made with Altair) to your portfolio page.
