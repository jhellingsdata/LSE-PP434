# Editing your site in VSCode (Week 1 seminar)

By the end of this seminar you should have:

- [ ] Your site's files open in VSCode, previewed with Live Server
- [ ] A portfolio page with **3 charts** embedded
- [ ] Your name and links in place of the placeholder text
- [ ] The changes live on your website

Before you start, complete the [Getting started guide](00-getting-started.md), including the Live Server extension.

> **This week is temporary.** We download a copy of the site and upload changes through the browser. Next week, Git replaces both steps with a single click in VSCode.

---

## 1. Download your site and open it in VSCode

1. Go to your repository, `github.com/USERNAME/USERNAME.github.io`.
2. Click the green **Code** button → **Download ZIP**.
3. Unzip it. You get a folder called `USERNAME.github.io-main`.
4. In VSCode: **File → Open Folder…** and choose that folder.

Your files appear in the **Explorer** panel on the left.

---

## 2. Preview with Live Server

1. In the Explorer, right-click `index.html` → **Open with Live Server**. You can also click **Go Live** in the bar at the bottom right.
2. Your page opens in the browser at an address like `127.0.0.1:5500`. This preview is only on your computer and nobody else can see it.
3. Make a small change to `index.html` and save it (`Cmd + S` / `Ctrl + S`). The preview updates instantly.

---

## 3. Rename your pages

Web addresses are **case-sensitive**, so we use lowercase names with no spaces.

1. In the Explorer, right-click `Example3.html` → **Rename** and call it `portfolio.html`. Your portfolio page will then be at `USERNAME.github.io/portfolio`.
2. Add a link to it on your home page (`index.html`), inside the `<body>`:

   ```html
   <p><a href="portfolio.html">See my portfolio</a></p>
   ```

---

## 4. Embed charts

Each chart needs two things, linked by the same `id`:

1. **A place on the page for the chart:**
   ```html
   <figure id="Location2"></figure>
   ```
2. **A script that puts the chart there:**
   ```js
   let figure_2_spec = "chart1.json";
   vegaEmbed('#Location2', figure_2_spec);
   ```

There are two ways to point to a chart spec:

| | Example | When to use it |
|---|---|---|
| **Local (relative) link** | `"chart1.json"` | The spec file is in your own repository, in the same folder as the page |
| **Raw GitHub link** | `"https://raw.githubusercontent.com/…/chart.json"` | The spec is in someone else's GitHub repository. Open the file on GitHub, click **Raw**, and copy the address. |

Add **two more charts** to `portfolio.html` so it has three in total: one from the [Week 1 examples](../weeks/week01/examples/) and one from:

- [Economics Observatory data vis (Substack charts)](https://github.com/EconomicsObservatory/datavis)
- [Economics Observatory visualisations](https://github.com/EconomicsObservatory/ECOvisualisations)
- [Richard's chart library](https://rdeconomist.github.io/library)

> If a chart doesn't appear, check that the `id` in the `<figure>` matches the one in `vegaEmbed` (including the `#`), and that the file name or URL is spelt exactly right.

---

## 5. Make it yours

Replace the placeholder text in `portfolio.html`: your name, the LinkedIn and GitHub links, and the descriptions. You can also edit `index.html` into a short home page about you.

---

## 6. Publish your changes

1. On your repository page: **Add file → Upload files**.
2. Drag in the files you changed (e.g. `index.html`, `portfolio.html`, any `.json` files) and click **Commit changes**.
3. **Delete the old page.** Renaming on your computer doesn't rename the file on GitHub, so `Example3.html` is still there. Open it on GitHub, click **⋯ → Delete file**, then **Commit changes**.
4. After a minute or two, check `USERNAME.github.io` and `USERNAME.github.io/portfolio`.

Keeping track of which files changed, and tidying up renamed files, is exactly what Git does for you. We set it up next week.

---

**Next:** [Setting up Git](02-git-setup.md), before the Week 2 seminar.
