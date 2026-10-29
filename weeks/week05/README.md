# Week 5: Programming · Loops and conditionals

**Lecture practical:** Loops, conditionals, and downloading many data series at once
**Seminar:** JavaScript loops: building a mini dashboard

## Notebooks

Click **Open in Colab**, then **File → Save a copy in Drive** before you start.

| # | Notebook | Open | When | What it covers |
|---|---|---|---|---|
| 1 | [`DS5_1_Loops_QuickStart`](notebooks/DS5_1_Loops_QuickStart.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week05/notebooks/DS5_1_Loops_QuickStart.ipynb) | **Core**: lecture practical | `for` loops, f-strings, `if`/`else`, and a conditional inside a loop. Annex: the older `.format()` method |
| 2 | [`DS5_2_Loop_API_Download`](notebooks/DS5_2_Loop_API_Download.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week05/notebooks/DS5_2_Loop_API_Download.ipynb) | **Core**: lecture practical | Download six FRED series of your choice with a loop, check each request, save JSON files (portfolio CC6, part 1). Optional: keep your API key secret with Colab Secrets or a `.env` file |
| 2 | [`DS5_2_Loop_API_Download_Clean`](notebooks/DS5_2_Loop_API_Download_Clean.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week05/notebooks/DS5_2_Loop_API_Download_Clean.ipynb) | Reference | The same process in four short cells, without explanations |
| 3 | [`DS5_3_Loop_Charts_Altair`](notebooks/DS5_3_Loop_Charts_Altair.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week05/notebooks/DS5_3_Loop_Charts_Altair.ipynb) | Seminar / practice | A chart is a dictionary: loop over countries to make and save one chart each, with a conditional to highlight one |
| 4 | [`DS5_4_PythonBasics_LoopsConditionals`](notebooks/DS5_4_PythonBasics_LoopsConditionals.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week05/notebooks/DS5_4_PythonBasics_LoopsConditionals.ipynb) | Practice | Loops and conditionals in more depth: `range`, `elif`, `and`/`or`, `while`, `break`/`continue` ([solutions](notebooks/DS5_4_PythonBasics_LoopsConditionals_Solutions.ipynb)) |
| 5 | [`DS5_5_Loops_UsefulPatterns`](notebooks/DS5_5_Loops_UsefulPatterns.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week05/notebooks/DS5_5_Loops_UsefulPatterns.ipynb) | Practice | Three patterns for real work: building a list with `.append()`, pausing between API requests with `time.sleep()`, and a summary report of your downloaded files |
| 6 | [`DS5_6_Cleaning_Gilts`](notebooks/DS5_6_Cleaning_Gilts.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week05/notebooks/DS5_6_Cleaning_Gilts.ipynb) | Stretch: lecture example | Cleaning messy data (lecture Example 1, the UK gilt market): split names like `0 1/8% Treasury Gilt 2023` into coupon, type and year with string functions, a loop and `if` statements, then chart the result |

## Dashboards (JavaScript loops)

Three levels, from simple to advanced. Download the files in a dashboard (HTML, plus any `.js`, `.css` and `.json` with the same name) into one folder, and open the HTML with Live Server.

| Dashboard | Files | What the loop does |
|---|---|---|
| **1. One chart per file** | [`dashboard1_fred_files.html`](dashboards/dashboard1_fred_files.html) + [`dashboard_styles.css`](dashboards/dashboard_styles.css) | Loops over your list of six FRED series codes. Each time, it puts the file link and title into a template chart and embeds it in the next `<figure>`. **This is portfolio task CC6, part 2.** |
| **2. Inflation checker** | [`dashboard2_inflation_checker.html`](dashboards/dashboard2_inflation_checker.html) + [`.js`](dashboards/dashboard2_inflation_checker.js) | You type in country codes. The loop builds an Economics Observatory API link for each, and **creates** a new box on the page for each chart |
| **3. Chart builder** | [`dashboard3_chart_builder.html`](dashboards/dashboard3_chart_builder.html) + [`.js`](dashboards/dashboard3_chart_builder.js) + [`dataHub_seriesToCountries.json`](dashboards/dataHub_seriesToCountries.json) | As 2, plus a choice of data series and a button listing the countries available for it |

Dashboard 1 uses **your** data: put the six JSON files you downloaded with DS5_2 in a `data` folder next to the HTML file, and your series codes in `seriesCodes`.

## Conditionals in charts (Vega-Lite)

| Chart | What it shows |
|---|---|
| [`conditional_colour.json`](examples/conditional_colour.json) | Colour each bar red **if** a value is above 5%, otherwise grey (`"condition"` and `"test"`) |
| [`conditional_ternary.json`](examples/conditional_ternary.json) | A ternary conditional (`condition ? if_true : if_false`) makes a new column, then we colour by it |
| [`conditional_diverging.json`](examples/conditional_diverging.json) | Red **if** GDP growth is negative, otherwise teal. `lag` gets the previous quarter, to work out the % change |
| [`conditional_three_levels.json`](examples/conditional_three_levels.json) | A **nested** ternary for three groups: inflation over 4%, 2% to 4%, or at or below 2% |
| [`conditional_labels.json`](examples/conditional_labels.json) | Label only the bars that matter: the label text is empty (`''`) **unless** the value is above 5% |
| [`conditional_hover.json`](examples/conditional_hover.json) | *Preview of Week 8 (interactive charts), optional:* a bar is solid **if** the mouse is over it, faded otherwise |
| [`conditional_latest_point.json`](examples/conditional_latest_point.json) | Mark and label only the **latest** value: a `filter` keeps the row whose date equals the latest date. Updates by itself when new data arrives |

The first two use a few annual values typed into the chart; the others use the course data in [`data/`](data/). Each chart's `description` explains how it works.

**Altair versions:** [`conditional_charts_altair.py`](examples/conditional_charts_altair.py) makes all seven charts in Python, using `alt.when(...).then(...).otherwise(...)` (Altair's if/else). Read it side by side with the `.json` files, or run it to save each chart.

The dashboards also use a conditional: a `filter` transform keeps only the data from 2000 onwards.

## Data

[`data/`](data/): six FRED series (downloaded October 2025), used by some of the example charts. To build your own dashboard, download your own choice of series with DS5_2: our code doesn't point to these files automatically.

## API keys

FRED needs an API key. FRED keys are free and easy to replace, so our notebooks and live charts use a shared course key, and it's fine for a FRED key to appear in a public chart. For **paid or private** keys, keep them out of public repositories and websites. DS5_2 shows how to keep a key secret: Colab's **Secrets** in Colab, or a **`.env`** file on your own computer (already listed in the course `.gitignore`).

## Tips for writing loops

1. Get the steps working for **one** item first, without a loop.
2. Then loop over **two** items, and only then the full list.
3. Put `print()` (Python) or `console.log()` (JavaScript) inside the loop to see how far it gets.
