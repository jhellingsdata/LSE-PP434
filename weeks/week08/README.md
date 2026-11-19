# Week 8: Big data

**Lecture practical:** Making charts when you have too much data: 12.8 million menu prices

## The data: menu prices

The LSE Growth Lab collected **3.3 million photos of menus**, posted with Google Maps reviews in 25 UK city regions, and used large language models to read the prices: **12.8 million prices** from about 80,000 cafes, pubs and restaurants, from 2011 to 2026 (most from 2017). It's part of the AutoCPI project, which uses web data to measure prices in more detail than official statistics can.

The full dataset is too big for class, so [`data/`](data/) has smaller slices. Venues are anonymous: there are no venue names or Google ids, and locations are rounded to about 100 m.

For your chart footnotes: **Source: LSE Growth Lab, AutoCPI (menu photos)**.

## Notebooks

Click **Open in Colab**, then **File → Save a copy in Drive** before you start. Start with DS8_1.

| Notebook | Open | What it covers |
|---|---|---|
| [`DS8_1_Menu_Prices_QuickStart`](notebooks/DS8_1_Menu_Prices_QuickStart.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week08/notebooks/DS8_1_Menu_Prices_QuickStart.ipynb) | 270,000 prices, already summarised into a 56 KB CSV. The price of a latte since 2017, which of 12 well-known items rose most since 2019, and a map: is a latte dearer in London? |
| [`DS8_2_Price_of_a_Pint`](notebooks/DS8_2_Price_of_a_Pint.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week08/notebooks/DS8_2_Price_of_a_Pint.ipynb) | The prices themselves: 220,000 beer and cider prices. Reading only the columns you need, cleaning text to find a pint, medians by year, city and chain, then maps by region and pub by pub |

## Data

In [`data/`](data/). Read a `.parquet` file with `pd.read_parquet()`, just like `pd.read_csv()`. In Colab it works straight away; on your own computer, install `pyarrow` first (`uv pip install pyarrow`).

| File | Rows | What it is |
|---|---:|---|
| [`menu_iconic_by_year_region.csv`](data/menu_iconic_by_year_region.csv) | 1,202 | The median price of 12 items (latte, flat white, cappuccino, fish & chips, margherita, cheeseburger, chicken tikka masala, english breakfast, guinness, sausage roll, croissant, pad thai) by year and ITL1 region, plus the UK (`itl1_id` = `UK`). `prices` is how many prices each median comes from; regions need at least 20 |
| [`menu_iconic_items.parquet`](data/menu_iconic_items.parquet) | 273,700 | Every price for those 12 items |
| [`menu_beer_cider.parquet`](data/menu_beer_cider.parquet) | 221,388 | Every beer and cider price, with a `size` where the menu gave one |
| [`menu_quotes_sample.parquet`](data/menu_quotes_sample.parquet) | 632,478 | Every price at a random 5% of venues (4,041 venues), so you can follow a menu over time |
| [`cities/menu_wales.parquet`](data/cities/) | 633,579 | Every price in one city region. Also `menu_glasgow` (420,852), `menu_bristol` (194,188), `menu_york` (102,295) and `menu_hull` (74,177) |

Every `.parquet` file has these columns:

| Column | What it is |
|---|---|
| `venue_id` | An anonymous code for each venue |
| `vtype` | Venue type: `Restaurant`, `Takeaway & fast food`, `Cafe & coffee`, `Pub & bar`, `Bakery & dessert`, `Other` |
| `chain_type`, `chain` | `independent`, `branded` (a named chain), `managed estate` (pub companies such as Wetherspoon) or `hotel`; `chain` is the chain's name |
| `site` | The city region the venue was collected in (25, e.g. `london`, `west-midlands`, `glasgow`) |
| `itl1_id`, `itl1` | The venue's ITL1 region (2025), with the same codes as map-data's [`ITL1_UK_2025.json`](https://github.com/jhellingsdata/map-data) (`properties.id`) |
| `lat`, `lng` | Location, rounded to 3 decimal places (about 100 m) |
| `item` | The item as written on the menu. Where it included the venue's name, the name is replaced by `[venue]` |
| `canon` | The standard name for the dish or drink, e.g. `latte`, `guinness` |
| `group`, `course` | Its type (`Coffee & hot drinks`, `Beer & cider`, `Indian & South Asian`, ...) and course (`main`, `starter`, `side`, `dessert`, `drink`, ...) |
| `price` | Price in £ |
| `date` | The date the photo was taken |

**Things to watch:**

- **Not the whole UK.** The data comes from 25 city regions, so a region's figure describes its cities (e.g. "East" is mostly Norwich).
- **More photos every year.** About 1,500 latte prices in 2017, 23,000 in 2025, and fewer in 2020 and 2021. Check the `count` behind every median.
- **Who's in the mix.** Wetherspoon's median pint is about £3.75, against £5.50 at independents. A city with more Wetherspoons *looks* cheaper. Comparing the same item at the same venue over time avoids this.
- **Odd prices.** Menus are read by AI, so some prices are wrong. Keep a sensible range (e.g. `price.between(0.5, 100)`).

## Tips for big data

1. **Read less.** `pd.read_parquet(file, columns=[...])` reads only the columns you need, and uses less memory.
2. **Summarise before you chart.** Every row you chart is saved inside the chart. `groupby(...).agg(["median", "count"])` turns 93,000 pints into 10 rows.
3. **Too many rows for Altair?** Altair stops at 5,000 rows. `alt.data_transformers.disable_max_rows()` turns the limit off, but a chart of 100,000 points is a slow, multi-MB file: summarise, sample (`df.sample(5000)`) or make the points see-through (`opacity=0.1`).
4. **Split it up.** One small chart per group (`.facet()`), or a dropdown to pick one (`alt.binding_select`).
5. **Small numbers.** Leave out medians from only a few prices: they're noisy, and with private data they can reveal individuals.
