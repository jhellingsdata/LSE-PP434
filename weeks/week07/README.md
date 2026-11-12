# Week 7: Maps

**Lecture practical:** Point maps: putting data on a base map with layers
**Seminar:** Choropleth maps: colouring areas with a lookup, and mapping devolution

## 🗺️ The maps page

**[Week 7 maps page](https://jhellingsdata.github.io/LSE-PP434/weeks/week07/maps/)**: every example below, with an explanation, the chart and its code. Open any chart in the Vega Editor from its **…** menu.

## Notebook

Click **Open in Colab**, then **File → Save a copy in Drive** before you start.

| Notebook | Open | What it covers |
|---|---|---|
| [`DS7_1_Maps_Altair`](notebooks/DS7_1_Maps_Altair.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jhellingsdata/LSE-PP434/blob/main/weeks/week07/notebooks/DS7_1_Maps_Altair.ipynb) | The same maps in Python: base maps, layered point maps, choropleths with a lookup, and strategic authorities |

## Lecture practical: step by step

From an x/y chart to a map, in [`examples/lecture/`](examples/lecture/):

| Step | Chart | The idea |
|---|---|---|
| 1 | [`L1_airports_as_a_scatter_plot`](examples/lecture/L1_airports_as_a_scatter_plot.json) | Longitude and latitude are just x and y, in degrees. The shape looks squashed |
| 2 | [`L2_airports_with_a_projection`](examples/lecture/L2_airports_with_a_projection.json) | A projection is an x/y scale for the whole Earth: degrees → pixels |
| 3 | [`L3_base_map`](examples/lecture/L3_base_map.json) | A base map is more coordinates, drawn as shapes with the same projection |
| 4 | [`L4_layers`](examples/lecture/L4_layers.json) | Map + points in one chart: a `layer`, sharing one projection |
| 5 | [`L5_size_and_tooltip`](examples/lecture/L5_size_and_tooltip.json) | Encode passengers as size, add a tooltip |
| 6 | [`L6_finished`](examples/lecture/L6_finished.json) | Title, council borders, circle outlines |

## Vega-Lite examples

Each builds on the one before. Copy one into the [Vega Editor](https://vega.github.io/editor/) to try it.

**1. Base maps**

| Chart | What's new |
|---|---|
| [`DS7_01_wales_outline`](examples/DS7_01_wales_outline.json) | One shape, a `geoshape` mark and a projection. TopoJSON needs `"format": {"type": "topojson", "feature": "geog"}` |
| [`DS7_02_wales_local_authorities`](examples/DS7_02_wales_local_authorities.json) | Many shapes; a tooltip shows each shape's `properties` |
| [`DS7_03_uk_nations`](examples/DS7_03_uk_nations.json) | Colour by a property in the map file itself |
| [`DS7_16_geojson_wales`](examples/DS7_16_geojson_wales.json) | **GeoJSON**, as you'll often find online: `"format": {"property": "features"}`, and ONS-style property names (`LAD13CD`) |
| [`DS7_17_geojson_choropleth`](examples/DS7_17_geojson_choropleth.json) | The same file simplified with mapshaper (1.5 MB → 85 KB), as a choropleth |

**2. Point maps (layers)**

| Chart | What's new |
|---|---|
| [`DS7_04_airports_points`](examples/DS7_04_airports_points.json) | Points from a CSV with `latitude` and `longitude`, sized by passengers |
| [`DS7_05_airports_layered`](examples/DS7_05_airports_layered.json) | A `layer`: base map underneath, points on top. One projection, set at the top |
| [`DS7_06_power_plants`](examples/DS7_06_power_plants.json) | Colour and size together; a `sqrt` size scale |

**3. Choropleth maps (lookups)**

| Chart | What's new |
|---|---|
| [`DS7_07_lookup_basics`](examples/DS7_07_lookup_basics.json) | A `lookup` on its own: joining two small tables on a code |
| [`DS7_08_wales_wages_choropleth`](examples/DS7_08_wales_wages_choropleth.json) | Start with the map, look up a value for each area from a CSV with **one row per area**. Missing data in grey |
| [`DS7_09_wales_wages_many_years`](examples/DS7_09_wales_wages_many_years.json) | When the CSV has **many years**: start with the CSV, filter to a year, then look up the shapes (`"as": "geo"` and the `shape` encoding) |

**4. Devolution**

| Chart | What's new |
|---|---|
| [`DS7_10_england_strategic_authorities`](examples/DS7_10_england_strategic_authorities.json) | England's strategic authorities in July 2026, by tier, over a grey layer of all councils |
| [`DS7_11_wales_cjc`](examples/DS7_11_wales_cjc.json) | A lookup with categories: Wales's councils by Corporate Joint Committee, with the four CJC borders (merged in mapshaper) on top |
| [`DS7_12_strategic_authority_density`](examples/DS7_12_strategic_authority_density.json) | Zoom in on one strategic authority: small areas coloured by a lookup, with council borders as an outline layer. **A template for the portfolio task** |
| [`DS7_20_strategic_authority_choropleth`](examples/DS7_20_strategic_authority_choropleth.json) | A choropleth of the strategic authorities themselves, from `msa_latest.csv` (one row per authority, one column per indicator). Change the column to map another indicator |

**5. Going further**

| Chart | What's new |
|---|---|
| [`DS7_13_wales_msoa_density`](examples/DS7_13_wales_msoa_density.json) | Small areas (408 MSOAs) and a log colour scale |
| [`DS7_14_scotland_wages`](examples/DS7_14_scotland_wages.json) | The "many years" pattern for Scotland |
| [`DS7_15_world_gdp`](examples/DS7_15_world_gdp.json) | A world map, the Equal Earth projection, and matching on ISO3 country codes |
| [`DS7_18_devolution_budget_2026`](examples/DS7_18_devolution_budget_2026.json) | England's devolution map as set out at Budget 2026: in force, agreed, proposed and named areas |
| [`DS7_19_constituencies_2024`](examples/DS7_19_constituencies_2024.json) | The 650 Westminster constituencies; a `calculate` turns the first letter of each code into its nation. Add election results with a lookup |

## Map files

All map files come from **[jhellingsdata/map-data](https://github.com/jhellingsdata/map-data)**, a collection of simplified TopoJSON files: UK nations, councils, ITL regions, census areas, constituencies, strategic authorities and the world. In every file the shapes are in the group `geog`, and each area has an `id` code and a `name`.

- [Which file do I need?](https://github.com/jhellingsdata/map-data/blob/main/README.md) · [Filtering to Wales, a region or an authority](https://github.com/jhellingsdata/map-data/blob/main/gbr/README.md) · [Strategic authorities guide](https://github.com/jhellingsdata/map-data/blob/main/gbr/sa/README.md)
- Raw links look like `https://raw.githubusercontent.com/jhellingsdata/map-data/refs/heads/main/gbr/LAD_WLS_2026_05.json`

## Data

In [`data/`](data/). Most files have three columns: `geo_id` (the area code), `value` and `date`.

**For mapping devolution in England (and Wales):** [`data/msa/`](data/msa/README.md) has ready-to-map data for every strategic authority and council: GVA, pay, employment, degrees, life expectancy, child poverty, deprivation, emissions and more, plus small-area house prices, commuting and deprivation. Its [README](data/msa/README.md) explains which map file goes with each file.

Also in `data/`:

| File | What | Areas |
|---|---|---|
| `wales_wages_2024.csv` | Wages, 2024 only (one row per area) | Wales councils |
| `wages_LAD_WLS.csv`, `wages_LAD_SCT.csv` | Wages, 2008–2024 | Wales / Scotland councils |
| `unemp_LAD_*.csv`, `gdp_per_head_LAD_*.csv`, `labour_productivity_LAD_*.csv`, `pct65_plus_LAD_*.csv`, `anxiety_LAD_*.csv` | More indicators to try, many dates | Wales / Scotland councils |
| `pop_density_census_msoa21.csv` | Population density (people per km²), 2021 Census | England and Wales MSOAs |
| `wales_pop_density_msoa.csv`, `wales_house_prices_msoa.csv` | Population density, house prices | Wales MSOAs |
| `wales_cjc_lookup.csv` | Each Welsh council's Corporate Joint Committee | Wales councils |
| `wales_cjc.json` | The four CJC regions (TopoJSON, made in mapshaper by merging councils) | Wales CJCs |
| `wales_councils_simplified.geojson` | Wales's councils as GeoJSON, simplified from [martinjc/UK-GeoJSON](https://github.com/martinjc/UK-GeoJSON) | Wales councils |
| `uk_airports.csv` | Passengers and flights, with latitude and longitude | Points |
| `uk_power_plants.csv` | Capacity and fuel, with latitude and longitude | Points |
| `world_gdp_per_capita_2022.csv` | GDP per person (PPP), World Bank | Countries (ISO3 codes) |

## Tips for maps

1. **Nothing appears?** Check the data `format`. TopoJSON needs the right `feature` name (`geog` for map-data files); GeoJSON needs `"property": "features"`.
2. **Colours missing?** The codes in your map and your CSV must match exactly. Add a tooltip with `properties.id` to see the map's codes.
3. **Wrong year, or blank?** A lookup keeps one row per area. Use a CSV with one row per area, or the "many years" pattern (DS7_09).
4. **Slow to load?** Map files over about 500 KB slow your page down. Simplify them with [mapshaper.org](https://mapshaper.org): see our **[mapshaper guide](../../setup/05-map-files-mapshaper.md)**.
5. **A filled rectangle, or a blank map?** See "Common problems" in the mapshaper guide: usually the order of the points (GeoJSON from mapshaper: export with `gj2008`) or British National Grid coordinates.
