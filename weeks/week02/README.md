# Week 2: Making your point with data

**Lecture practical:** Vega-Lite editor, the ECO Data Hub, finding your own data, adapting a chart
**Seminar:** Cleaning ONS data, adapting and styling a line chart, embedding it on your site

**Portfolio task:** add **two new charts that you have made** to your portfolio page (5 charts in total).

## Files

| File | What it is |
|---|---|
| [`data/cpih_ons_raw.csv`](data/cpih_ons_raw.csv) | UK inflation (CPIH annual rate, series L55O), exactly as downloaded from the ONS |
| [`data/cpih_monthly.csv`](data/cpih_monthly.csv) | The same data after cleaning: monthly only, columns `date` and `cpih`, dates as `yyyy-mm-dd` |
| [`examples/cpih_line_basic.json`](examples/cpih_line_basic.json) | The simplest possible line chart: data, mark, x and y |
| [`examples/cpih_line_styled.json`](examples/cpih_line_styled.json) | The same chart with a few styling properties added |
| [`examples/cpih_line_ons_raw.json`](examples/cpih_line_ons_raw.json) | *Optional, advanced:* charts the raw ONS file directly, with no Excel cleaning |

> The chart files load their data from a raw GitHub link. When you adapt them, replace the `"url"` with the raw link to **your** CSV file.

---

## 1. Clean the ONS data

ONS downloads stack **annual**, **quarterly** and **monthly** values in one column, below 8 rows of information about the series. A chart needs **one row per date and one type of data per column**.

Open `cpih_ons_raw.csv` in Excel:

1. **Keep only the monthly rows.** Monthly data starts at `1989 JAN` (row 196). Select rows **1–195** (click row header 1, then Shift-click row header 195), right-click → **Delete**.
2. **Add column names.** Right-click row 1 → **Insert**. Type `date` in A1 and `cpih` in B1. Use short lowercase names with no spaces, because you will type them in your chart.
3. **Fix the dates** using one of the methods below.
4. **Save as CSV.** **File → Save As** → *CSV UTF-8 (Comma delimited)*.

### Fixing `1989 JAN`-style dates

Vega-Lite needs dates like `1989-01-01`.

> First, check what Excel did when it opened the file. Click a date cell and look at the formula bar. If Excel already converted `1989 JAN` into a real date, skip to the last step and just change the format.

**Option A, the easiest: fill a monthly series.** This needs no formulas.

1. In **C2**, type `1989-01-01`.
2. Select C2 down to the last row of data.
3. **Home → Fill → Series** → *Type:* **Date**, *Date unit:* **Month** → **OK**.
4. **Check the last row** says `2026-08-01`, matching `2026 AUG` in column A. If it doesn't, a month is missing somewhere.
5. Delete column A. Your new dates are now in column A.
6. **Set the format:** select the date column → right-click → **Format Cells** → **Custom** → type `yyyy-mm-dd`.

**Option B: a formula.** This works for any list of dates, even with gaps, but only in English-language Excel.

1. In C2, enter `=DATEVALUE("1 "&RIGHT(A2,3)&" "&LEFT(A2,4))` and double-click the fill handle to copy it down.
2. Copy column C, then **Paste Special → Values** over the top of it.
3. Delete column A and set the format to `yyyy-mm-dd`, as in Option A.

> **Why set the format?** A CSV saves dates exactly as Excel *displays* them. If the cell shows `01/02/1989`, that is what gets saved, and it's ambiguous: is it 1 February (UK) or 2 January (US)? `yyyy-mm-dd` is never ambiguous.

Finally, upload the CSV to your repository and copy its **Raw** link.

---

## 2. Adapt a basic line chart

Start from [`cpih_line_basic.json`](examples/cpih_line_basic.json), or a simple line chart from the [Vega-Lite examples](https://vega.github.io/vega-lite/examples/) or the [chart library](https://rdeconomist.github.io/library). Paste it into the [Vega-Lite editor](https://vega.github.io/editor/) and change three things:

1. `"url"`: your raw CSV link
2. The x `"field"`: your date column name (`date`)
3. The y `"field"`: your value column name (`cpih`)

Remove anything else you don't need. If the chart is blank, the column names probably don't match the CSV headers exactly (they are case-sensitive).

---

## 3. Style it: change 5 properties

Styling properties live in **three places** in a chart spec:

| Where | What it controls | Examples |
|---|---|---|
| **Top level** | The whole chart | `"title"`, `"width"`, `"height"` |
| **`"mark"`** | The line, bars or points | `"color"`, `"strokeWidth"` |
| **`"axis"`** (inside x or y) | One axis | `"title"`, `"grid"`, `"labelExpr"`, `"labelFontSize"` |

To style the mark, turn `"mark": "line"` into an object: `"mark": {"type": "line", "color": "#c8102e"}`.

**Task:** change at least 5 of these:

- [ ] A title that states the finding (e.g. *"UK inflation peaked at 9.6% in October 2022"*), not just the topic
- [ ] A subtitle with the units and the **source**
- [ ] Line colour
- [ ] Line width (`strokeWidth`)
- [ ] Chart size (`width`, `height`)
- [ ] Remove axis titles that the title already explains (`"title": null`)
- [ ] Remove the vertical grid lines (`"grid": false` on the x axis)
- [ ] Add `%` to the y-axis labels (`"labelExpr": "datum.value + '%'"`)

Compare yours with [`cpih_line_styled.json`](examples/cpih_line_styled.json). The [Vega-Lite documentation](https://vega.github.io/vega-lite/docs/) has every option: see the *Title*, *Mark* and *Axis* pages.

---

## 4. Add it to your site

1. In the editor, copy the full spec. Save it in your site folder in VSCode as a `.json` file (e.g. `cpih_chart.json`).
2. In `portfolio.html`, add a new `<figure id="...">` and a `vegaEmbed` line pointing to the file. This is the same pattern as Week 1.
3. Check it with Live Server, then upload the changed files to GitHub.

Repeat with a second dataset of your own for your second chart.

---

## Common problems

| Problem | Fix |
|---|---|
| **Chart is blank in the editor** | Check the field names match the CSV headers exactly, and the URL is the **Raw** link (`raw.githubusercontent.com/...`) |
| **Dates appear as 1970, or as numbers** | Annual data like `1989` is read as a number, not a date. Either make it `1989-01-01` in Excel, or add `"format": {"parse": {"date": "date:'%Y'"}}` inside `"data"` (where `date` is your column name) |
| **Numbers are wrong or missing** (e.g. `3,3` instead of `3.3`) | Your computer uses an international number format. See the [international formats guide](https://github.com/jhellingsdata/jhellingsdata.github.io/tree/main/examples/vega-lite/international-formats) |
| **Chart from the ECO Data Hub shows in the editor but not on your site** | Data Hub charts use `"width": "container"`. Change it to a number, e.g. `"width": 400` |
| **The site doesn't update** | GitHub Pages takes a minute or two. Then hard-refresh: `Cmd + Shift + R` (Mac) / `Ctrl + Shift + R` (Windows) |
