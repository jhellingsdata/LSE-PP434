# Data for mapping England's strategic authorities

Ready-to-map data for England's **strategic authorities** (SAs) and their councils. Every file
uses the same codes as the [map-data](https://github.com/jhellingsdata/map-data) map files, so a
`lookup` works with no cleaning.

Strategic authorities are not an official statistical area, so most data isn't published for
them. We have done that work for you: each SA figure is either published for that exact area or
built from its councils' figures by a method checked against published figures. None is a simple
average of its councils.

Most files have three columns, like the rest of the week's data: `geo_id` (the area code),
`value` and `date`.

## Which map file goes with which data?

All map links start with `https://raw.githubusercontent.com/jhellingsdata/map-data/refs/heads/main/gbr/`

| Data files ending… | Areas | Map file |
|---|---|---|
| `_MSA_ENG.csv`, `msa_latest.csv` | Strategic authorities (`MSA001` to `MSA022`) | `SA_ENG_2026_07.json` (the 20 in force in July 2026), or `proposed/SA_ENG_2025_12.json` (22, adding Greater Essex and Norfolk and Suffolk) |
| `_LAD_ENG.csv` | English councils (`E06`… to `E09`…) | `LAD_ENG_2026_05.json`, or one SA's councils: `sa/msa001_greater_manchester/LAD.json` |
| `_LAD_WLS.csv` | Welsh councils (`W06`…) | `LAD_WLS_2026_05.json` |
| `_MSOA_ENG.csv` | Small areas: MSOAs (`E02`…) | One SA's small areas: `sa/msa004_south_yorkshire/MSOA.json` |
| `_LSOA_ENG.csv` | Smaller areas: LSOAs (`E01`…) | `sa/msa004_south_yorkshire/LSOA.json` |

The `sa/` folder names are listed in the [strategic authorities guide](https://github.com/jhellingsdata/map-data/blob/main/gbr/sa/README.md).

## The indicators

Each indicator has an SA file and a file for every English council. Four also have a Welsh
council file, for those mapping Wales.

| File name starts… | What it measures | Dates | England, latest | Source | Wales file |
|---|---|---|---|---|---|
| `gva_per_head` | Economic output (GVA) per resident, £, current prices | 1998 to 2024 | £38,095 | ONS regional accounts | |
| `pay_fulltime` | Median annual pay of full-time workers who live in the area, £ | 2002 to 2026 (councils from 2008) | £41,140 | ONS Annual Survey of Hours and Earnings | |
| `employment_rate` | % of residents aged 16 to 64 in work | 2004 to 2025 | 75.8% | ONS Annual Population Survey | ✓ |
| `degree_level` | % of residents aged 16 to 64 qualified to degree level or above (RQF4+) | 2022 to 2025 | 48.0% | ONS Annual Population Survey | ✓ |
| `old_age_dependency` | Residents aged 65+ for every 100 aged 16 to 64 | 1991 to 2025 | 30.3 | ONS mid-year population estimates | |
| `life_expectancy_female`, `life_expectancy_male` | Life expectancy at birth, years | 2001-2003 to 2022-2024 | 83.3 (women), 79.5 (men) | ONS life expectancy for local areas | ✓ |
| `child_poverty` | % of children (0 to 15) in relative low income families, after housing costs | 2023/24 to 2024/25 | 27.1% | DWP Children in low income families | |
| `most_deprived_10pct` | % of residents living in England's most deprived 10% of neighbourhoods | 2025 | 10.0% (by definition) | MHCLG English Indices of Deprivation 2025 | |
| `emissions_per_head` | Greenhouse gas emissions per resident, tonnes CO2e | 2005 to 2024 | 4.7 | DESNZ local authority emissions | |

**Dates.** Most are years. `2024/25` is a financial year (April 2024 to March 2025). Life
expectancy is measured over three years, so `2022-2024` is one period. Filter on the text exactly
as it appears, e.g. `"filter": "datum.date == '2022-2024'"`.

### One row per SA: `msa_latest.csv`

Every SA's latest value for each indicator, one column each, with its `name`, `short` name,
`tier` (July 2026) and `region`. One row per area means you can look up straight from the map
(the DS7_08 pattern), and copy several columns at once with `"fields"`. Starter chart:
[`DS7_20_strategic_authority_choropleth`](../../examples/DS7_20_strategic_authority_choropleth.json).

### Small areas, for zooming in on one SA

| File | What it measures | Date | Source |
|---|---|---|---|
| `house_prices_MSOA_ENG.csv` | Median house price, all homes, £ | Year to September 2025 | ONS house price statistics for small areas |
| `sustainable_commute_MSOA_ENG.csv` | % of commuters who go by bus, train, tram, bike or on foot (people working from home left out) | Census 2021 | ONS Census 2021 |
| `imd_decile_LSOA_ENG.csv` | Deprivation decile: 1 = England's most deprived 10% of neighbourhoods, 10 = least deprived | 2025 | MHCLG English Indices of Deprivation 2025 |

These have two columns (`geo_id`, `value`) and cover all of England. Use them with the DS7_12
template: change the folder name and the CSV link. Population density is in the main `data/`
folder (`pop_density_census_msoa21.csv`).

## Things to know

- **Codes.** SAs have no official code, so each has an `MSA0xx` code (map-data's `id`). One code
  is always the same group of councils. Greater London (`MSA022`) uses the figures for the
  London region, which covers exactly the same area.
- **Missing areas.** Show them in grey. West of England has no GVA figure, and neither do
  15 councils in the South West: ONS withdrew those figures after finding an error and has not
  yet republished them. The Isles of Scilly is too small for the surveys behind employment,
  degrees and pay, and the City of London has no pay figures. Neither has life expectancy figures.
- **The City of London is an outlier.** Fewer than 10,000 people live there, but hundreds of
  thousands work there. So its figures per resident are extreme (GVA per head in the millions of
  pounds, high emissions per head), and survey figures are based on very few people (an
  employment rate of 100% in some years). Consider leaving it out with a filter on its code,
  `E09000001`, or say so in your notes.
- **Greater Essex (`MSA013`) and Norfolk and Suffolk (`MSA021`)** have data but no shape on the
  July 2026 map, because they were not yet in force. They appear on the `proposed/` maps.
- **London stands out.** Its GVA per resident is far above everywhere else, so it takes up most
  of the colour scale. Try a different scale type, or say so in your subtitle.
- **Don't average councils to get an SA.** In a simple average, a council with 30,000 people
  counts as much as one with 500,000. That's why we give you the SA figures.
- **Council codes.** Council files use the councils on the May 2026 map. Most sources have
  re-published their older years on today's council boundaries, so the "many years" maps stay
  complete; the pay data for Cumberland and Westmorland and Furness starts in 2022. Barnsley and
  Sheffield were given new codes in 2025 with no change of boundary; we have moved their figures
  to the new codes.

## Where the data comes from

Extracted from the msa-data research warehouse in November 2026, using the same figures as its
briefings. Where ONS publishes a figure for exactly the SA's area (a combined authority or ITL2
region), we use it. Otherwise we build one from the councils: adding up counts (people,
emissions, children in low income families) and recalculating the rate, pooling councils' pay
distributions, or, for life expectancy, weighting each council by its population. To rebuild:
`uv run python analysis/teaching/pp434_week7_maps.py` in msa-data.
