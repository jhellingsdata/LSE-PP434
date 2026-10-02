# Getting started (Week 1)

In the Week 1 lecture practical you created your GitHub account and your website. This guide checks that everything is in place and installs what you need for the **Week 1 seminar**.

By the end you will have:

- [ ] A GitHub account, with your email kept private
- [ ] A live website at `https://USERNAME.github.io`
- [ ] VSCode installed
- [ ] The browser tools we use in class

If you get stuck, note which step and the exact error message, and bring it to the seminar or office hours.

---

## 1. Check your GitHub account and website

*You did this in the lecture practical. If you missed it, follow the steps in brackets.*

- [ ] **You can sign in at [github.com](https://github.com/).** *(Sign up there. Your username becomes your website address, so pick something professional you'd be happy to put on a CV.)*
- [ ] **You have a repository called `USERNAME.github.io`,** where `USERNAME` is your **exact** GitHub username. *(Click **+ → New repository**, type that name, set it to **Public**, tick **Add a README file**, then click **Create repository**.)*
- [ ] **It contains an `index.html` file** (the example page you renamed in the lecture) and `Example3.html`.
- [ ] **`https://USERNAME.github.io` shows your page.** Changes can take a minute or two to appear.

> **Your repository vs your website.** Your *repository* (`github.com/USERNAME/USERNAME.github.io`) is where your files are stored. Your *website* (`USERNAME.github.io`) is what the world sees. GitHub Pages builds the website from the repository's files.

### Keep your email private

Your website repository is public. Before we start saving changes from VSCode (from Week 2), stop your email address from showing on them:

1. On GitHub, click your profile picture → **Settings → Emails**.
2. Tick **"Keep my email addresses private"**.

---

## 2. Install VSCode

VSCode is the code editor we use for the whole course. Download it from [code.visualstudio.com](https://code.visualstudio.com/).

**Mac**
1. Open the downloaded `.zip` (it unzips to *Visual Studio Code.app*).
2. **Drag *Visual Studio Code* into your *Applications* folder.** Don't run it from *Downloads*: it can fail to update and cause problems later.
3. Open it from *Applications* (or with Spotlight: `Cmd + Space`, type "Visual Studio Code").

**Windows**
1. Run the downloaded **User Installer**.
2. Keep the defaults, and make sure **"Add to PATH"** is ticked. We also recommend ticking both **"Add 'Open with Code' action"** boxes.

### Install the Live Server extension

Live Server shows your page in the browser and refreshes it every time you save, so you can check changes before publishing them.

1. In VSCode, click the **Extensions** icon in the left sidebar (four small squares), or press `Cmd + Shift + X` (Mac) / `Ctrl + Shift + X` (Windows).
2. Search for **Live Server** (by Ritwick Dey) and click **Install**.

---

## 3. Browser tools

You'll use these throughout the course. Sign in or bookmark each one:

- **[Vega-Lite editor](https://vega.github.io/editor/):** where we test chart specifications.
- **[Economics Observatory](https://www.economicsobservatory.com/):** create a Data Hub account (used in portfolio task CC2).
- **[Google Colab](https://colab.research.google.com/):** sign in with a Google account. We will mainly run Python in VSCode, but Colab is our backup.
- **Richard's course site, [rdeconomist.github.io](https://rdeconomist.github.io):** right-click anywhere and choose **Inspect** to see the HTML behind the page.
  - *Safari users:* first turn on **Safari → Settings → Advanced → "Show features for web developers"**.
- **Viewing JSON:** we often look at raw data returned by APIs.
  - Chrome can display it neatly: tick **"Pretty-print"** at the top of a JSON page.
  - Alternatively, install a *JSON Formatter* extension from the Chrome Web Store.
  - Firefox has a JSON viewer built in.

---

## Next

- **Week 1 seminar:** [Editing your site in VSCode](01-editing-in-vscode.md)
- **Before the Week 2 seminar:** [Setting up Git](02-git-setup.md)
