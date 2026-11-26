# Week 9: Advanced analysis and interactivity

**Lecture practical:** making charts interactive: widgets (dropdowns, radio buttons, sliders, checkboxes) and selections (hover, legend, brush)

Copy any example into the [Vega Editor](https://vega.github.io/editor/) to try it. All data is in [`data/`](data/); maps come from [map-data](https://github.com/jhellingsdata/map-data).

## Notebooks

Click **Open in Colab**, then **File → Save a copy in Drive** before you start.

| Notebook | Open | What it covers |
|---|---|---|
| [`DS9_1_Interactive_Charts`](notebooks/DS9_1_Interactive_Charts.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week09/notebooks/DS9_1_Interactive_Charts.ipynb) | The lecture practical in Altair: widgets (dropdown, radio buttons, range slider, checkbox, colour picker) and selections (hover, clickable legend, brush to zoom), then a slider with a legend, a dropdown map and a re-indexing slider |
| [`DS9_2_Analytical_Charts`](notebooks/DS9_2_Analytical_Charts.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week09/notebooks/DS9_2_Analytical_Charts.ipynb) | The lecture's analytical charts, with the pandas steps: rebasing, small multiples, moving averages, trends and the gaps from them, regression and loess lines, distributions, an event study (UK productivity) and error bars |

## Analytical charts (lecture section 9.2)

New Vega-Lite examples, one technique each, in [`examples/analysis/`](examples/analysis/). The transforms do the analysis inside the chart.

| Chart | What's new |
|---|---|
| [`A1_rebasing`](examples/analysis/A1_rebasing.json) | Rebasing to 2019 = 100: `calculate` keeps the base-year price, `joinaggregate` copies it to every row of the same dish, a second `calculate` divides |
| [`A2_trellis_independent`](examples/analysis/A2_trellis_independent.json) | Small multiples (`facet`) with independent y-axes (`resolve`), for series at different levels |
| [`A3_moving_average`](examples/analysis/A3_moving_average.json) | A centred 31-day moving average: `window` with `frame: [-15, 15]` |
| [`A4_trend_deviations`](examples/analysis/A4_trend_deviations.json) | A log-linear trend, and each quarter's gap from it, with the least squares done in two `joinaggregate`s. Recessions shaded |
| [`A5_scatter_fit`](examples/analysis/A5_scatter_fit.json) | A scatter with a straight-line fit (`regression`) and a smooth one (`loess`) |
| [`A6_distributions`](examples/analysis/A6_distributions.json) | Histogram (`bin`), density (`density` with `groupby`) and box plot (`boxplot`) of the same data |
| [`A7_event_study`](examples/analysis/A7_event_study.json) | An event study: UK productivity against its pre-2008 trend, fitted on 1997-2007 only and extended. The gap is shaded |

## Lecture practical: making charts interactive

So far we've used tooltips. This week: two kinds of interactivity, built one step at a time in [`examples/lecture/`](examples/lecture/).

- **Widgets:** the reader sets a value with a control under the chart (a dropdown, radio buttons, a slider, a checkbox).
- **Selections:** the reader acts on the chart itself (hovering, clicking the legend, dragging a brush).

Every interaction is **a param** (a named value) **plus a place that uses it** (a filter, a calculation, a condition, a title). The recipe for a widget: hard-code a value, give it a name as a param (the chart doesn't change), then add `bind` to get the control.

Data: the Week 8 menu prices summary, [`menu_percentiles_by_year.csv`](../week08/data/menu_percentiles_by_year.csv) (one row per dish and year, with the 10th, 25th, 50th, 75th and 90th percentile price), and the ONS long-run price index for the brush.

**Widgets**

| Chart | The idea |
|---|---|
| [`W0_start`](examples/lecture/W0_start.json) | Start: one dish, hard-coded in the filter ('latte'). Every widget below replaces a hard-coded value like this with a param. |
| [`W1_dropdown`](examples/lecture/W1_dropdown.json) | 1. Dropdown: a param bound to a 'select' input. Recipe: (1) give the hard-coded value a name, a param with a value; (2) use the param where the value was: datum.item == dish; (3) add 'bind' to get a widget. Don't call the param 'item': Vega reserves it. |
| [`W2_radio`](examples/lecture/W2_radio.json) | 2. Radio buttons: a second param picks which column to plot. 'calculate': 'datum[measure]' copies the chosen column into 'value', and the chart plots 'value'. 'labels' shows readable names for the options. |
| [`W3_range_slider`](examples/lecture/W3_range_slider.json) | 3. Range slider: a number param bound to a 'range' input, with min, max and step. Here it sets the first year shown: filter datum.year >= startYear. |
| [`W4_checkbox`](examples/lecture/W4_checkbox.json) | 4. Checkbox: a true/false param bound to a 'checkbox' input. Here it shows or hides a layer: the band's opacity is an expression, showRange ? 1 : 0. |

**Selections**

| Chart | The idea |
|---|---|
| [`S1_hover_highlight`](examples/lecture/S1_hover_highlight.json) | 5. Hover highlight: a 'point' selection on the dish, triggered by the pointer. Recipe: (1) add a select param; (2) use it in a condition: opacity 1 when selected, 0.15 otherwise; (3) choose the trigger ('on': 'pointerover', 'nearest': true finds the closest point). With 'empty': true (the default), every line is full strength until you hover. The selection sits on the points layer, which comes first: a selection needs points to pick from, and S2 binds it to the legend, which only works from the first layer. |
| [`S2_legend_click`](examples/lecture/S2_legend_click.json) | 6. Clickable legend: S1 with two changes. (1) Colour by dish: a legend only exists when an encoding (colour, size, shape...) makes one, so S1, with every line brown, has no legend to click. The colour encoding also splits the lines, so 'detail' goes. (2) In the selection, replace 'on' and 'nearest' with 'bind': 'legend'. (The selection must sit on the first layer for the legend binding to work: that's why S1 puts the points layer first.) Click a dish in the legend (shift-click for more than one); double-click the chart to reset. |
| [`S3_brush_zoom`](examples/lecture/S3_brush_zoom.json) | 7. Brush to zoom: an 'interval' selection on x in the small chart (drag across it; double-click to reset). The big chart keeps only the rows inside the brush: {"filter": {"param": "brush"}}, so both axes fit the years you picked. Two views, one above the other (vconcat). Another way: "scale": {"domain": {"param": "brush"}} on the big chart's x. |

**Stretch: a rebasing explorer.** The same data, step by step to a chart with a dropdown, a range band and a slider that rebases prices to any year.

| Chart | The idea |
|---|---|
| [`L1_median_line`](examples/lecture/L1_median_line.json) | Step 1 (the starting chart): the median price of a latte each year. 'calculate' makes a date from the year, for the time axis. |
| [`L2_pick_a_dish`](examples/lecture/L2_pick_a_dish.json) | Step 2: a param bound to a dropdown ('select' input). The filter now uses the param (datum.item == dish), so the reader picks the dish. The title uses it too, through an expression. Don't call the param 'item': Vega reserves that name. |
| [`L3_add_the_range`](examples/lecture/L3_add_the_range.json) | Step 3: a layer. An area from the 10th to the 90th percentile (y and y2) sits under the median line, so the chart shows the spread, not just the middle. |
| [`L4_rebase_slider`](examples/lecture/L4_rebase_slider.json) | Step 4 (finished): rebase with a slider. Mark the base year's price ('calculate' with a condition), copy it to every row ('joinaggregate' with max, which ignores the nulls), then divide: median / base * 100. Every dish is 100 in the base year, so dishes become comparable. |

> **Watch out:** don't call a param `item`. Vega reserves that name, and the chart fails with "item is not defined".

## Interactive charts (lecture section 9.4)

The lecture's figures 1 to 11, plus five new interactive maps (12 to 16), in [`examples/interactive/`](examples/interactive/).

| Chart | What it shows |
|---|---|
| [`DS9_01_tooltip_single`](examples/interactive/DS9_01_tooltip_single.json) | A tooltip with one field: hover over a bar to see its value. |
| [`DS9_02_tooltip_multi`](examples/interactive/DS9_02_tooltip_multi.json) | A tooltip with several fields, each with its own title and format. |
| [`DS9_03_input_colour`](examples/interactive/DS9_03_input_colour.json) | A colour picker: a param bound to a 'color' input sets the line colour. A colour input needs a hex value, such as #ff0000. (Saved copy of the ONS data: see the file for the live link.) |
| [`DS9_04_input_text_colour`](examples/interactive/DS9_04_input_text_colour.json) | The same with a text box: type any CSS colour (red, magenta, rgb(10,30,150)). (Saved copy of the ONS data: see the file for the live link.) |
| [`DS9_05_input_text_filter`](examples/interactive/DS9_05_input_text_filter.json) | Two text boxes set the first and last year; a filter transform uses them. (Saved copy of the ONS data: see the file for the live link.) |
| [`DS9_05b_input_text_filter`](examples/interactive/DS9_05b_input_text_filter.json) | As 05, a second version of the text-box year filter. (Saved copy of the ONS data: see the file for the live link.) |
| [`DS9_06_range_filter`](examples/interactive/DS9_06_range_filter.json) | Two range sliders set the first and last year shown. |
| [`DS9_06b_range_filter_select`](examples/interactive/DS9_06b_range_filter_select.json) | One slider picks a single year (a Gapminder-style bubble chart); clicking the legend picks a region. |
| [`DS9_07_range_reindex`](examples/interactive/DS9_07_range_reindex.json) | Re-indexing with a slider: pick a start year and every value is divided by that year's value (x 100). A 'window' transform with first_value finds the start year's value. The data is the ONS long-run price index, rebuilt from the annual inflation series (CDSI) and extended with CDKO, saved in the repo so the chart doesn't depend on the ONS website. |
| [`DS9_08_selection_dropdown_map`](examples/interactive/DS9_08_selection_dropdown_map.json) | A dropdown picks the series to map. The param holds a column name; 'calculate': 'datum[SelectParam]' copies that column into varSelected, which the colour uses. Map: map-data's ITL3 areas (TopoJSON), matched on properties.id. |
| [`DS9_09_hover_select`](examples/interactive/DS9_09_hover_select.json) | Highlight on hover: a point selection on 'Country', and an opacity condition. Many lines, one picked out. |
| [`DS9_10_checkbox`](examples/interactive/DS9_10_checkbox.json) | A checkbox: starts the y-axis at zero, using a condition in the scale's domainMin. |
| [`DS9_10b_checkbox_layers`](examples/interactive/DS9_10b_checkbox_layers.json) | The checkbox chart with extra layers: recession bands and a shaded recovery gap. |
| [`DS9_10c_checkbox_slider`](examples/interactive/DS9_10c_checkbox_slider.json) | The checkbox and a year slider together. |
| [`DS9_11_hover_select_concat`](examples/interactive/DS9_11_hover_select_concat.json) | Linked views: hover a borough on the map or a point on the scatter, and it's highlighted in both. Both views define the same point selection (point_paintbrush) on Name. Map: map-data's Greater London boroughs, matched on the ONS code. |
| [`DS9_12_dropdown_map`](examples/interactive/DS9_12_dropdown_map.json) | New. A dropdown picks the dish to map (menu prices by region, 2025). The data has one row per dish, year and region, so the chart starts from the CSV, filters, then looks up each region's shape (Week 7's DS7_09 pattern). |
| [`DS9_13_year_slider_map`](examples/interactive/DS9_13_year_slider_map.json) | New. A range slider picks the year (the price of a latte by region, 2017-2026). The colour scale has a fixed domain, so the map darkens as prices rise. |
| [`DS9_14_dropdown_slider_map`](examples/interactive/DS9_14_dropdown_slider_map.json) | New. Both together. One colour scale can't fit every dish and year, so colour shows each region against the UK median for the same dish and year ('joinaggregate'). |
| [`DS9_15_wales_explorer`](examples/interactive/DS9_15_wales_explorer.json) | New. A regional explorer for Wales's 22 councils, with Week 7's data: a dropdown picks the indicator (pay, GDP per head, productivity, unemployment, employment, aged 65+, anxiety), a slider picks the map's year, and hovering a council picks out its line in the chart beside it. Data: [`wales_indicators_LAD.csv`](data/wales_indicators_LAD.csv). |
| [`DS9_16_strategic_authorities_explorer`](examples/interactive/DS9_16_strategic_authorities_explorer.json) | New. England's strategic authorities, with Week 7's `msa_latest.csv`: a dropdown picks one of ten indicators for the map and a ranked bar chart. One hover selection, defined once at the top with `views`, links the two. |

## Uncertainty (seminar)

Error bars, error bands and fan charts, in [`examples/uncertainty/`](examples/uncertainty/).

| Chart | What it shows |
|---|---|
| [`DS9_20_error_bars_simple`](examples/uncertainty/DS9_20_error_bars_simple.json) | Error bars from a table of results: a point for the estimate (Beta), a rule from the lower to the upper 95% confidence interval (y and y2). Economics Observatory, youth club closures. |
| [`DS9_21_error_bars_two_methods`](examples/uncertainty/DS9_21_error_bars_two_methods.json) | Two estimation methods side by side, using xOffset. |
| [`DS9_22_fan_chart_simple`](examples/uncertainty/DS9_22_fan_chart_simple.json) | A fan chart: forecast lines with bands for the 10th-90th percentile ranges. OBR, October 2026 (with the March 2026 forecast for comparison). |
| [`DS9_23_fan_chart_styled`](examples/uncertainty/DS9_23_fan_chart_styled.json) | The same fan chart, styled. |

## More practice

Last year's practical, in [`examples/practice/`](examples/practice/): each has a **start** file without the interactivity, and a **finished** file.

| Chart | What to do |
|---|---|
| [`P1_hover_scatter_finished`](examples/practice/P1_hover_scatter_finished.json) | Practice 1, finished: a point selection on hover, with conditional size and opacity. |
| [`P1_hover_scatter_start`](examples/practice/P1_hover_scatter_start.json) | Practice 1, start: a scatter of US states. Add a hover highlight. |
| [`P2_hover_bars_finished`](examples/practice/P2_hover_bars_finished.json) | Practice 2, finished: hover highlight on bars. |
| [`P2_hover_bars_start`](examples/practice/P2_hover_bars_start.json) | Practice 2, start: a bar chart. Add a hover highlight. |
| [`P3_year_slider_finished`](examples/practice/P3_year_slider_finished.json) | Practice 3, finished: a range slider picks the year; clicking the legend picks a region. |
| [`P3_year_slider_start`](examples/practice/P3_year_slider_start.json) | Practice 3, start: GDP and maternal mortality, every year at once. Add a year slider. |

## Data

| File | What | Source |
|---|---|---|
| `youth_unemployment_2021.csv` | Youth unemployment, 21 most populous countries, 2021 | World Bank |
| `gdp_life_expectancy.csv` | GDP per person and life expectancy, by country | World Bank, UN |
| `ons_rpi_inflation_long_run.json` | RPI annual inflation, 1800-2020 (ONS series CDSI, saved copy) | ONS |
| `uk_prices_long_run.csv` | RPI price index, 1800-2025 (1974 = 100): rebuilt from CDSI to 2020, then extended with the long-run index CDKO | ONS |
| `bitcoin_price.csv` | Daily Bitcoin price, US dollars | Investing.com |
| `maternal_mortality_gdp.json` | Maternal mortality and GDP per person, by country and year | WHO, World Bank |
| `itl3_indicators.csv` | Population, GDP, employment and more, for the UK's ITL3 areas | *to add* |
| `gdp_trajectories.csv` | GDP per person since 1960, by country | World Bank |
| `us_real_gdp_per_capita.csv`, `us_recessions.json` | US real GDP per person; US recession dates | FRED; recession dates *to add* |
| `council_finances_2023.csv` | Council borrowing, assets and population change, 2023 | *to add* |
| `us_states_socioeconomic.csv` | US states: median income and firearm deaths | *to add* |
| `wales_indicators_LAD.csv` | Seven indicators for Wales's 22 councils (and Wales, where published), 2004-2025, in one long table: council, indicator, year, value. Built from Week 7's Wales files; unemployment is the year to December | ONS |
| `uk_productivity.csv` | UK output per hour worked, whole economy, 1997-2025 (2024 = 100) | ONS (LZVB), 17 November 2026 |
| `youth_clubs_crime_effects.csv` | Effect of youth club closures on crime, with 95% confidence intervals | Economics Observatory |
| `obr_growth_forecasts.csv`, `obr_growth_uncertainty_ranges.csv` | UK GDP growth forecasts and their uncertainty ranges: the October 2026 forecast (with March 2026), from `data_raw/` (chart 2.12) | OBR |
