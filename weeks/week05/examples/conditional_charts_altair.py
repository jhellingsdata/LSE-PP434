"""
Conditionals in charts: the Altair (Python) versions
====================================================

Each chart below is the Altair version of one of the Vega-Lite (.json) examples in this folder.
Compare them side by side: Altair writes the same Vega-Lite settings, but in Python.

The key tool is alt.when(...).then(...).otherwise(...), which reads just like if / else:
    alt.when(alt.datum.value > 5).then(alt.value("red")).otherwise(alt.value("grey"))
    = "when the value is above 5, make it red, otherwise grey"
(Older code uses alt.condition(test, if_true, if_false), which does the same thing.)

We use Altair's "method" syntax: settings are chained on with dots, e.g. alt.Y("value:Q").title(None),
rather than written inside the brackets, e.g. alt.Y("value:Q", title=None). Both make the same chart.

To run it: pip install altair --upgrade   (we use Altair 6, which writes Vega-Lite v6)
           python conditional_charts_altair.py
It saves each chart as an .html file (open in a browser) and a .json file (for your website).
In a notebook, you can instead just put a chart's name on the last line of a cell to show it.
"""

import altair as alt

RED, GREY, TEAL = "#c8102e", "#bbbbbb", "#58b3c7"
BASE = "https://raw.githubusercontent.com/jhellingsdata/LSE-PP434/main/weeks/week05/data/"


def fred_data(code):
    """The link to one of the course FRED files. The data is inside "observations"."""
    return alt.Data(url=f"{BASE}data_US_FRED-{code}.json", format={"type": "json", "property": "observations"})


def title(text, subtitle):
    return alt.Title(text, subtitle=subtitle, anchor="start", subtitleFontSize=10, subtitleColor="grey")


years = list(range(2015, 2025))


# 1. conditional_colour.json: colour IF a value is above 5 ------------------------------------
unemployment = [5.3, 4.9, 4.4, 3.9, 3.7, 8.1, 5.4, 3.6, 3.6, 4.0]

chart_colour = alt.Chart(
    alt.Data(values=[{"year": y, "value": v} for y, v in zip(years, unemployment)]),
    title=title("When was US unemployment above 5%?",
                "Unemployment rate, %, annual average. Red: above 5%. Source: FRED (UNRATE)"),
    width=400, height=220,
).mark_bar().encode(
    x=alt.X("year:O").title(None).axis(labelAngle=0),
    y=alt.Y("value:Q").title(None),
    color=alt.when(alt.datum.value > 5).then(alt.value(RED)).otherwise(alt.value(GREY)),
).configure_view(stroke="transparent")


# 2. conditional_ternary.json: a ternary makes a new column, then we colour by it -------------
fed_funds = [0.13, 0.40, 1.00, 1.83, 2.16, 0.38, 0.08, 1.68, 5.02, 5.14]

chart_ternary = alt.Chart(
    alt.Data(values=[{"year": y, "value": v} for y, v in zip(years, fed_funds)]),
    title=title("When were US interest rates above 2%?",
                "Federal funds rate, %, annual average. Source: FRED (FEDFUNDS)"),
    width=400, height=220,
).transform_calculate(
    Level="datum.value > 2 ? 'Above 2%' : '2% or below'"      # the same text as in the .json
).mark_bar().encode(
    x=alt.X("year:O").title(None).axis(labelAngle=0),
    y=alt.Y("value:Q").title(None),
    color=alt.Color("Level:N").title(None).scale(domain=["Above 2%", "2% or below"], range=[RED, GREY]),
).configure_view(stroke="transparent")


# 3. conditional_diverging.json: red IF growth is negative ------------------------------------
chart_diverging = alt.Chart(
    fred_data("GDPC1"),
    title=title("When did the US economy shrink?",
                "Real GDP, % change on previous quarter. Red: the economy shrank. Source: FRED (GDPC1)"),
    width=450, height=220,
).transform_window(
    previous="lag(value)", sort=[{"field": "date"}]                  # the previous quarter's value
).transform_calculate(
    growth="(toNumber(datum.value) / toNumber(datum.previous) - 1) * 100"
).transform_filter(
    "year(datum.date) >= 2005"
).mark_bar().encode(
    x=alt.X("date:T").title(None).axis(grid=False),
    y=alt.Y("growth:Q").title(None),
    color=alt.when(alt.datum.growth < 0).then(alt.value(RED)).otherwise(alt.value(TEAL)),
    tooltip=[alt.Tooltip("date:T").format("%b %Y").title("Quarter"),
             alt.Tooltip("growth:Q").format(".1f").title("Growth, %")],
).configure_view(stroke="transparent")


# 4. conditional_three_levels.json: a nested ternary gives three groups -------------------------
chart_three_levels = alt.Chart(
    fred_data("CPIAUCSL"),
    title=title("How far was US inflation from the 2% target?",
                "Consumer prices, % change on a year earlier. Source: FRED (CPIAUCSL)"),
    width=450, height=220,
).transform_window(
    window=[{"op": "lag", "param": 12, "field": "value", "as": "year_ago"}],   # the value 12 months earlier
    sort=[{"field": "date"}]
).transform_calculate(
    inflation="(toNumber(datum.value) / toNumber(datum.year_ago) - 1) * 100"
).transform_filter(
    "year(datum.date) >= 2015"
).transform_calculate(
    Level="datum.inflation > 4 ? 'Over 4%' : datum.inflation > 2 ? '2% to 4%' : 'At or below 2%'"
).mark_bar().encode(
    x=alt.X("date:T").title(None).axis(grid=False),
    y=alt.Y("inflation:Q").title(None),
    color=alt.Color("Level:N").title(None).scale(domain=["Over 4%", "2% to 4%", "At or below 2%"],
                                                 range=[RED, "#f4a582", GREY]),
    tooltip=[alt.Tooltip("date:T").format("%b %Y").title("Month"),
             alt.Tooltip("inflation:Q").format(".1f").title("Inflation, %"), "Level:N"],
).configure_view(stroke="transparent")


# 5. conditional_labels.json: label only the bars above 5% --------------------------------------
annual_unemployment = alt.Chart(
    fred_data("UNRATE"),
).transform_calculate(
    rate="toNumber(datum.value)"
).transform_timeunit(
    year="year(date)"
).transform_aggregate(
    rate="mean(rate)", groupby=["year"]
).transform_filter(
    "year(datum.year) >= 2005 && year(datum.year) <= 2024"
).transform_calculate(
    label="datum.rate > 5 ? format(datum.rate, '.1f') : ''"        # empty text IF not above 5
).encode(
    x=alt.X("year(year):O").title(None).axis(labelAngle=0, labelExpr="year(datum.value) % 5 == 0 ? datum.label : ''"),
    y=alt.Y("rate:Q").title(None),
)

bars = annual_unemployment.mark_bar().encode(
    color=alt.when(alt.datum.rate > 5).then(alt.value(RED)).otherwise(alt.value(GREY)))
labels = annual_unemployment.mark_text(dy=-6, fontSize=10, color=RED).encode(text="label:N")

chart_labels = (bars + labels).properties(
    title=title("Which years had unemployment above 5%?",
                "Unemployment rate, %, annual average. Labels: years above 5%. Source: FRED (UNRATE)"),
    width=450, height=220,
).configure_view(stroke="transparent")


# 6. conditional_hover.json: IF the mouse is over a bar, make it solid (PREVIEW of Week 8) ------
#    Interactive charts come in Week 8: you don't need this one yet.
hover = alt.selection_point(on="pointerover", clear="pointerout")    # remembers which bar is hovered

chart_hover = alt.Chart(
    fred_data("FEDFUNDS"),
    title=title("US interest rates since 2000",
                "Federal funds rate, %, annual average. Hover over a bar. Source: FRED (FEDFUNDS)"),
    width=450, height=220,
).transform_calculate(
    rate="toNumber(datum.value)"
).transform_timeunit(
    year="year(date)"
).transform_aggregate(
    rate="mean(rate)", groupby=["year"]
).transform_filter(
    "year(datum.year) >= 2000 && year(datum.year) <= 2024"
).mark_bar(color=TEAL).encode(
    x=alt.X("year(year):O").title(None).axis(labelAngle=0, labelExpr="year(datum.value) % 5 == 0 ? datum.label : ''"),
    y=alt.Y("rate:Q").title(None),
    opacity=alt.when(hover).then(alt.value(1)).otherwise(alt.value(0.3)),
    tooltip=[alt.Tooltip("year(year):O").title("Year"), alt.Tooltip("rate:Q").format(".2f").title("Rate, %")],
).add_params(hover).configure_view(stroke="transparent")


# 7. conditional_latest_point.json: mark and label only the latest value -----------------------
unemployment_monthly = alt.Chart(
    fred_data("UNRATE"),
).transform_calculate(
    rate="toNumber(datum.value)"
).transform_filter(
    "year(datum.date) >= 2015 && isValid(datum.rate) && isFinite(datum.rate)"
).transform_joinaggregate(
    latest_date="max(date)"                                          # adds the latest date to every row
).encode(
    x=alt.X("date:T").title(None).axis(grid=False),
    y=alt.Y("rate:Q").title(None),
)

line = unemployment_monthly.mark_line(color=GREY)
latest = unemployment_monthly.transform_filter("datum.date == datum.latest_date")   # keep only the latest row
point = latest.mark_point(filled=True, size=60, color=RED)
label = latest.mark_text(align="left", dx=6, fontWeight="bold", color=RED).encode(
    text=alt.Text("rate:Q").format(".1f"))

chart_latest_point = (line + point + label).properties(
    title=title("US unemployment rate", "%, monthly. Source: FRED (UNRATE)"),
    width=450, height=220,
).configure_view(stroke="transparent")


# Save every chart, with a loop -------------------------------------------------------------
charts = {
    "conditional_colour": chart_colour,
    "conditional_ternary": chart_ternary,
    "conditional_diverging": chart_diverging,
    "conditional_three_levels": chart_three_levels,
    "conditional_labels": chart_labels,
    "conditional_hover": chart_hover,
    "conditional_latest_point": chart_latest_point,
}

if __name__ == "__main__":
    for name, chart in charts.items():
        chart.save(f"{name}_altair.html")     # open in a browser to see the chart
        chart.save(f"{name}_altair.json")     # the Vega-Lite spec, to compare with the .json example
        print(f"Saved {name}_altair.html and {name}_altair.json")
