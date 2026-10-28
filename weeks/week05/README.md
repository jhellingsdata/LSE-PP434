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

These use a few annual values typed into the chart, so they work anywhere. Each chart's `description` says how to switch to one of your own FRED files.

The dashboards also use a conditional: a `filter` transform keeps only the data from 2000 onwards.

## API keys

FRED needs an API key. The notebooks use a shared course key so the demo works, but **never put your own key in a public repository, website or chart**. DS5_2 shows how to keep a key secret: Colab's **Secrets** in Colab, or a **`.env`** file on your own computer (already listed in the course `.gitignore`).

## Tips for writing loops

1. Get the steps working for **one** item first, without a loop.
2. Then loop over **two** items, and only then the full list.
3. Put `print()` (Python) or `console.log()` (JavaScript) inside the loop to see how far it gets.
