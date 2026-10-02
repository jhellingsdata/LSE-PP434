# Week 1: Introduction + building blocks

**Lecture practical:** Your first web page on GitHub Pages
**Seminar:** Editing your site in VSCode, Live Server, embedding charts

- Before the seminar: [Getting started](../../setup/00-getting-started.md)
- In the seminar: [Editing your site in VSCode](../../setup/01-editing-in-vscode.md)
- Before next week's seminar: [Setting up Git](../../setup/02-git-setup.md)

## Code examples

| File | What it shows |
|---|---|
| [`example1.html`](examples/example1.html) | The basic structure of an HTML page: `<head>`, `<body>`, headings, paragraphs and comments |
| [`example2.html`](examples/example2.html) + [`example2.css`](examples/example2.css) | Linking a CSS stylesheet to style the page |
| [`example3.html`](examples/example3.html) + [`example3.css`](examples/example3.css) | A starter portfolio page that embeds a Vega-Lite chart with `vegaEmbed` |
| [`chart1.json`](examples/chart1.json) | A bar chart with the data typed into the spec |
| [`chart2.json`](examples/chart2.json) | A line chart that loads its data from a CSV file online |

## In the lecture practical

1. Add one of the example pages to your `USERNAME.github.io` repository and **rename it to `index.html`**. `index.html` is always the home page of your site.
2. Add its CSS file, if it has one. The file name must match the `href` in the page's `<head>`.
3. Add the chart files and embed them in your page with `vegaEmbed`.
4. Visit `https://USERNAME.github.io` to check your live site. Updates can take a minute or two to appear.

## Useful links

- [Vega-Lite editor](https://vega.github.io/editor/): paste a chart spec to see what it looks like
- [Vega-Lite examples gallery](https://vega.github.io/vega-lite/examples/)
- [MDN HTML basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Creating_the_content)
