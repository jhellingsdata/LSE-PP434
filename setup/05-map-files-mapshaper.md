# Map files: finding, fixing and shrinking them with mapshaper

Map files you find online are often too big for a web page, in the wrong coordinates, or full of areas you don't need. [**mapshaper.org**](https://mapshaper.org) fixes all of these in your browser, with nothing to install.

This guide uses a real example: a file of Wales's 22 local authorities from [martinjc/UK-GeoJSON](https://github.com/martinjc/UK-GeoJSON), a popular source you may find first. It's **1.5 MB**. By the end, it's **17 KB** and looks the same on a web chart.

> **First, check [jhellingsdata/map-data](https://github.com/jhellingsdata/map-data).** It already has simplified TopoJSON files for UK nations, councils, ITL regions, census areas, constituencies and strategic authorities. You only need this guide for areas that aren't there.

## 1. Map file formats

| Format | What it is | In Vega-Lite |
|---|---|---|
| **GeoJSON** (`.geojson` or `.json`) | A list of `features`. Each has `geometry` (its coordinates) and `properties` (its name, code, …) | `"format": {"property": "features"}` |
| **TopoJSON** (`.json`) | Stores each shared border **once**, so it's much smaller | `"format": {"type": "topojson", "feature": "geog"}`, where `geog` is the name of the group of shapes in the file |
| **Shapefile** (`.shp` + `.dbf` + `.prj`, …) | An older format used by GIS software, as several files, often in a `.zip` | Not read directly: convert it with mapshaper |

## 2. Where to find boundaries

- **UK:** the [ONS Open Geography Portal](https://geoportal.statistics.gov.uk/). Each boundary comes in several versions. The letters at the end of the name tell you the detail:

  | Code | Detail | Use it for |
  |---|---|---|
  | **BUC** | Ultra generalised (500 m), clipped to the coastline | Whole-country web maps: start here |
  | **BGC** | Generalised (20 m), clipped to the coastline | Zoomed-in maps |
  | **BFC** / **BFE** | Full resolution, clipped to the coastline / to the extent of the realm | Calculations, not web charts |

  Download as **GeoJSON**.
- **Europe:** [Eurostat GISCO](https://ec.europa.eu/eurostat/web/gisco/geodata). **Worldwide:** [Natural Earth](https://www.naturalearthdata.com/), [UN GeoHub](https://geohub.data.undp.org/).
- Check the **year** of the boundaries matches your data: council borders change (Cumbria, North Yorkshire and Somerset were all reorganised in 2023, for example).

## 3. Simplify a file in the browser

1. Go to [mapshaper.org](https://mapshaper.org) and drag in your file (for a Shapefile, drag in the `.zip` or all its parts together). Click **Import**.
2. Look at the summary: click the **i** (info) or open the **Console** and type `info`. Check:
   - the **number of features** (22 for Welsh councils);
   - the **property names**, e.g. `LAD13CD` (the code) and `LAD13NM` (the name). You'll need the code for a lookup;
   - the **bounds**: longitude and latitude look like `-5.67, 51.37, -2.65, 53.44`. Big numbers like `146611, 164586` mean the file uses British National Grid (see section 5).
3. Click **Simplify**. Tick **prevent shape removal** (keeps small islands), then click **Apply**.
4. Drag the slider at the top. At around **5%**, the coastline is still clear at the size of a web chart. Zoom in to check; go back up if it looks jagged.
5. Click **Export**:
   - choose **TopoJSON** for the smallest file;
   - or **GeoJSON**, and type `gj2008` in the options box (see section 5 for why).

**Our result:** 1.5 MB → 85 KB as GeoJSON → **17 KB** as TopoJSON.

## 4. The console: the same, with commands

The **Console** button opens a command line. Commands are quicker to repeat, and you can save them with your project. The whole of section 3, plus tidying the properties, is:

```
-simplify 5% keep-shapes
-clean
-filter-fields LAD13CD,LAD13NM
-rename-fields id=LAD13CD,name=LAD13NM
-rename-layers geog
-o format=topojson wales_councils.json
```

| Command | What it does |
|---|---|
| `-simplify 5% keep-shapes` | Keep 5% of the points, without deleting small shapes |
| `-clean` | Fix small gaps and overlaps that simplifying can create |
| `-filter-fields a,b` | Keep only these properties (smaller file, tidier tooltips) |
| `-rename-fields new=old` | Rename properties, e.g. to match your other files |
| `-rename-layers geog` | Name the group of shapes. In TopoJSON, this is the `feature` name Vega-Lite needs |
| `-o format=topojson name.json` | Export (in the browser, this downloads the file) |

### Keep only some areas: `-filter`

Keep the areas whose code starts with `W` (Wales), from a UK-wide file:

```
-filter "LAD13CD.startsWith('W')"
```

The text in quotes is a JavaScript condition, as in Vega-Lite's `filter`. Property names are used directly.

### Merge areas: `-join` then `-dissolve`

To draw **regions made of councils**, such as Wales's Corporate Joint Committees (CJCs) or a strategic authority, merge the councils' shapes:

1. Add the region to each council, from a lookup table with one row per council. [`wales_cjc_lookup.csv`](../weeks/week07/data/wales_cjc_lookup.csv) has `lad_id`, `lad_name` and `cjc`.
2. Merge all the councils with the same region into one shape.

```
-join wales_cjc_lookup.csv keys=LAD13CD,lad_id fields=cjc
-dissolve cjc
-rename-layers geog
-o format=topojson wales_cjc.json
```

`keys=LAD13CD,lad_id` matches the map's `LAD13CD` to the CSV's `lad_id`: the same idea as a Vega-Lite `lookup`. The result, [`wales_cjc.json`](../weeks/week07/data/wales_cjc.json), is 10 KB and is used in the Week 7 example `DS7_11_wales_cjc`.

> In the browser, drag the CSV into mapshaper as well, so it can find it. If the join doesn't work there, use the command line (section 6).

## 5. Common problems, and fixes

| You see… | Why | Fix |
|---|---|---|
| **A filled rectangle** (the whole chart is one colour), or the map looks "inside out" | The shapes' points go round the wrong way. Vega-Lite expects the older GeoJSON order, but mapshaper exports the newer (RFC 7946) order by default | Export GeoJSON with `-o gj2008`, or export TopoJSON instead |
| **Nothing**, or a tiny dot | The file uses **British National Grid** (metres, numbers like `146611`), not longitude and latitude | `-proj wgs84`. If mapshaper can't tell what the file uses (no `.prj` file), tell it: `-proj wgs84 init=EPSG:27700` |
| **Gaps or slivers** between areas after simplifying | Simplifying moved shared borders | `-clean` |
| **Islands disappear** | Simplifying removed small shapes | `keep-shapes` (or "prevent shape removal") |
| **Colours missing** in a choropleth | Codes don't match: different years of boundaries, or different code columns | Check codes with `info` and a tooltip; use boundaries from the same year as your data |
| **The page is slow** | The file is still too big | Simplify more, export TopoJSON, keep fewer properties. Aim for under about 500 KB |

## 6. Optional: the command line

With [Node.js](https://nodejs.org) installed, the same commands run in a VSCode terminal, so the steps are saved and repeatable:

```bash
npx mapshaper -i lad.json \
  -simplify 5% keep-shapes -clean \
  -join wales_cjc_lookup.csv keys=LAD13CD,lad_id fields=cjc \
  -dissolve cjc -rename-layers geog \
  -o format=topojson wales_cjc.json
```

Add `-info` anywhere to print a summary at that point.

## Checklist before you use a map file

- [ ] It loads in the [Vega Editor](https://vega.github.io/editor/) with the right `format`
- [ ] It's in longitude and latitude (the map isn't blank or a tiny dot)
- [ ] It's under about 500 KB
- [ ] You know the name of its **code** property, and it matches your data
- [ ] The boundaries are from the same year as your data
- [ ] You've noted the source, for your chart's footnote

The mapshaper [command reference](https://github.com/mbloch/mapshaper/wiki/Command-Reference) lists every command.
