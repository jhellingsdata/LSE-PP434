# Setting up Git (before the Week 2 seminar)

From Week 2 we stop downloading and uploading files by hand. Instead, VSCode keeps your local copy and your live website connected through **Git**.

Complete steps 1–5 **before the Week 2 seminar**. It takes about 20 minutes. In the seminar we connect everything together (step 6).

- [ ] Your latest changes are on GitHub
- [ ] Git installed
- [ ] Git knows your name and (private) email
- [ ] A `.gitignore` file in your repository
- [ ] A `code` folder outside any cloud-synced location

If you get stuck, note which step and the exact error message, and come to office hours before the seminar.

---

## 1. Make sure GitHub has your latest work

In the seminar, you will download a fresh, connected copy of your site from GitHub. Anything that only exists in last week's downloaded folder will be left behind.

- [ ] Upload any changes you haven't published yet ([last week's step 6](01-editing-in-vscode.md#6-publish-your-changes)).
- [ ] Check your live site shows them.

After the seminar you can delete last week's `USERNAME.github.io-main` folder.

---

## 2. Install Git

Open a terminal in VSCode from the menu bar: **Terminal → New Terminal**. A panel opens at the bottom of the window with a blinking cursor, and this is where you type commands.

> *Shortcut:* `` Ctrl + ` `` (backtick) on both Mac and Windows. On a Mac this is **Control**, not Command. On UK Mac keyboards the backtick key is next to **Z**; on most Windows keyboards it is below **Esc**.

Check whether Git is already installed. Type this and press Enter:

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

## 3. Tell Git who you are

Git labels every change you save with a name and email. Set these now, so your first commit doesn't fail.

**First, find your private GitHub email.** On GitHub, go to **Settings → Emails**.
- Check **"Keep my email addresses private"** is ticked (you did this in Week 1).
- Copy the address shown underneath, which looks like `12345678+USERNAME@users.noreply.github.com`.

**Then, in the VSCode terminal,** run these two lines, **replacing the text in quotes**:

```
git config --global user.name "Your Name"
git config --global user.email "12345678+USERNAME@users.noreply.github.com"
```

Check it worked:

```
git config --global --list
```

You should see your `user.name` and `user.email`.

> Use the **noreply** address, not your personal email. Changes saved to a public repository can be seen by anyone.

---

## 4. Add a `.gitignore` to your repository

A `.gitignore` file lists files that Git should never upload, such as passwords, API keys and system clutter. We add it now, in the browser, so it is already in place when you connect VSCode.

1. On your repository page: **Add file → Create new file**.
2. Name the file `.gitignore` (starting with a dot).
3. Click **Choose .gitignore template** (it appears once you type the name) and select **Python**.
4. At the very bottom of the file, add this line (it hides a hidden file that Macs create in every folder):
   ```
   .DS_Store
   ```
5. Click **Commit changes**.

---

## 5. Choose where your code will live

In the seminar you will make a connected copy of your repository on your computer. Create a `code` folder for it now:

| | Use | Avoid |
|---|---|---|
| **Mac** | `/Users/YOURNAME/code` (make a `code` folder in your home folder) | Desktop, Documents (often synced to iCloud), iCloud Drive, OneDrive, Dropbox |
| **Windows** | `C:\Users\YOURNAME\code` | Documents or Desktop (often synced to OneDrive), OneDrive, Dropbox |

> **Why?** Cloud syncing tools and Git both try to manage your files, and they conflict. This is the most common cause of problems, so it's worth getting right from the start. Git already keeps your work safe on GitHub.

---

## Checklist

Run these in the VSCode terminal. Each should print something, not an error:

```
git --version
git config --global user.name
git config --global user.email
```

And check:

- [ ] Your repository on GitHub shows a `.gitignore` file
- [ ] You have a `code` folder outside any cloud-synced location

---

## 6. In the Week 2 seminar: connecting VSCode to GitHub

*We will do this together in the seminar. Full steps to follow.*

1. Sign in to GitHub from VSCode.
2. **Clone** your repository into your `code` folder. This makes a local copy that stays connected to GitHub.
3. Make a change, preview it with Live Server, then **commit** and **sync** it from the **Source Control** tab.

From then on, the rule is simple: **edit in VSCode, publish from Source Control, and never edit files directly on GitHub.**
