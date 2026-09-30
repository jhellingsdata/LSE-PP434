# Getting started (Week 0)

Complete this guide **before the Week 1 lecture**. It takes about 30–45 minutes, most of it waiting for downloads.

By the end you will have:

- [ ] VSCode installed
- [ ] Git installed and set up with your name and email
- [ ] A GitHub account and your website repository (`USERNAME.github.io`)
- [ ] The browser tools we use in class

If you get stuck, note which step and the exact error message, and bring it to the Week 1 practicals or office hours.

---

## 1. Install VSCode

Download from [code.visualstudio.com](https://code.visualstudio.com/).

**Mac**
1. Open the downloaded `.zip` (it unzips to *Visual Studio Code.app*).
2. **Drag *Visual Studio Code* into your *Applications* folder.** Don't run it from *Downloads*: it can fail to update and cause problems later.
3. Open it from *Applications* (or with Spotlight: `Cmd + Space`, type "Visual Studio Code").

**Windows**
1. Run the downloaded **User Installer**.
2. Keep the defaults, and make sure **"Add to PATH"** is ticked. We also recommend ticking both **"Add 'Open with Code' action"** boxes.

---

## 2. Install Git

Git tracks changes to your files and sends updates to your live website. First, check whether you already have it.

In VSCode, open a terminal from the menu bar: **Terminal → New Terminal**. A panel opens at the bottom of the window with a blinking cursor, and this is where you type commands.

> *Shortcut:* `` Ctrl + ` `` (backtick) on both Mac and Windows. On a Mac this is **Control**, not Command. On UK Mac keyboards the backtick key is next to **Z**; on most Windows keyboards it is below **Esc**.

Type:

```
git --version
```

If you see something like `git version 2.x.x`, skip to step 3.

**Mac**
- If Git isn't installed, the command above opens a pop-up asking to install the **Command Line Developer Tools**. Click **Install** and wait for it to finish (this can take several minutes).
- Then close and reopen VSCode and run `git --version` again.

**Windows**
- Download and run **Git for Windows** from [git-scm.com/downloads/win](https://git-scm.com/downloads/win).
- Keep the defaults with two exceptions:
  - *Choosing the default editor*: select **Visual Studio Code**.
  - *Adjusting the name of the initial branch*: select **Override** and keep **main**.
- *Alternative, if you're comfortable with the terminal:* `winget install --id Git.Git -e --source winget`
- **Close and reopen VSCode**, then run `git --version` again.

---

## 3. Create your GitHub account

Sign up at [github.com](https://github.com/).

> **Choose your username carefully.** It becomes your website address: `https://USERNAME.github.io`. Pick something professional that you'd be happy to put on a CV.

Once you're signed in, keep your email private (your website repository is public):

1. Go to **Settings → Emails**.
2. Tick **"Keep my email addresses private"**.
3. Copy the address shown underneath, which looks like `12345678+USERNAME@users.noreply.github.com`. You need it in the next step.

---

## 4. Tell Git who you are

Git labels every change you save with a name and email. Set these now, so your first commit in Week 1 doesn't fail.

In the VSCode terminal, run these two lines, **replacing the text in quotes**:

```
git config --global user.name "Your Name"
git config --global user.email "12345678+USERNAME@users.noreply.github.com"
```

Check it worked:

```
git config --global --list
```

You should see your `user.name` and `user.email`. Use the **noreply** email from step 3, not your personal one: commits on a public repository are visible to anyone.

---

## 5. Create your website repository

1. On GitHub, click **+ → New repository**.
2. **Repository name:** `USERNAME.github.io`. Replace `USERNAME` with your **exact** GitHub username (it must match, or your site won't work).
3. Set it to **Public**.
4. Tick **Add a README file**.
5. Under **Add .gitignore**, choose **Python**. This stops files that shouldn't be public (like passwords and settings files) from being uploaded later in the course.
6. Click **Create repository**.

That's all for now. In the Week 1 lecture we will add your first web page, and in the seminar we will connect this repository to VSCode.

---

## 6. Choose where your code will live

In Week 1 you will download a copy of your repository to your computer. Decide now where it will go:

| | Use | Avoid |
|---|---|---|
| **Mac** | `/Users/YOURNAME/code` (make a `code` folder in your home folder) | Desktop, Documents (often synced to iCloud), iCloud Drive, OneDrive, Dropbox |
| **Windows** | `C:\Users\YOURNAME\code` | Documents or Desktop (often synced to OneDrive), OneDrive, Dropbox |

> **Why?** Cloud syncing tools and Git both try to manage your files, and they conflict. This is the most common cause of problems, so it's worth getting right from the start. Git already keeps your work safe on GitHub.

---

## 7. Browser tools

You'll use these throughout the course. Sign in or bookmark each one:

- **[Vega-Lite editor](https://vega.github.io/editor/):** where we test chart specifications.
- **[Economics Observatory](https://www.economicsobservatory.com/):** create a Data Hub account (used in portfolio task CC2).
- **[Google Colab](https://colab.research.google.com/):** sign in with a Google account. We will mainly run Python in VSCode, but Colab is our backup.
- **Richard's course site, [rdeconomist.github.io](https://rdeconomist.github.io):** right-click anywhere and choose **Inspect** to see the HTML behind the page.
  - *Safari users:* first turn on **Safari → Settings → Advanced → "Show features for web developers"**.
- **Viewing JSON:** we often look at raw data returned by APIs.
  - Chrome can now display it neatly: tick **"Pretty-print"** at the top of a JSON page.
  - Alternatively, install a *JSON Formatter* extension from the Chrome Web Store.
  - Firefox has a JSON viewer built in.

---

## Final checklist

Run these in the VSCode terminal. Each should print something, not an error:

```
git --version
git config --global user.name
git config --global user.email
```

And check in your browser:

- [ ] `github.com/USERNAME/USERNAME.github.io` shows your repository with a README and `.gitignore`
- [ ] You have a `code` folder outside any cloud-synced location

You're ready for Week 1.
