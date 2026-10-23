# Running Python on your own computer (optional)

In class we use **Google Colab**, which needs no setup. This guide is for anyone who wants to go further and run the notebooks **in VSCode on your own computer**, next to your website files.

**Why bother?**
- Your notebooks, data and website are all in **one folder**. A notebook saves a CSV or chart, and Live Server shows it on your page straight away: no downloading and uploading.
- Your work is saved in your folder, and tracked by Git like everything else.
- It's how data work is usually done outside a classroom.

**It's optional.** Everything in the course works in Colab. If you get stuck, carry on in Colab and come to office hours.

Before you start, you need VSCode, Git and your website repository connected in VSCode ([Setting up Git](02-git-setup.md)). It takes about 15 minutes.

- [ ] `uv` installed
- [ ] VSCode's Python and Jupyter extensions installed
- [ ] A Python environment with the course packages, inside your website folder
- [ ] A notebook running in VSCode

---

## 1. Install `uv`

`uv` installs Python and the packages we use. We use it because it works the same way on Mac and Windows, and it installs Python for you.

Open a terminal in VSCode (**Terminal → New Terminal**) and run the line for your computer:

**Mac**
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows**
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Close and reopen VSCode**, then check it worked:
```
uv --version
```
You should see something like `uv 0.8.x`.

---

## 2. Install the VSCode extensions

Click the **Extensions** icon in the left sidebar (four small squares), then search for and install:

- **Python** (by Microsoft)
- **Jupyter** (by Microsoft)

---

## 3. Create a Python environment in your website folder

An **environment** is a private copy of Python, with the packages for one project. We keep it inside your website folder, in a hidden folder called `.venv`.

1. In VSCode, open your website folder (**File → Open Folder…**, then your `USERNAME.github.io` folder).
2. Download the course package list, [`requirements.txt`](requirements.txt): open it on GitHub, click the **Download raw file** button (the download icon at the top right of the file), and save it into your website folder.
3. In the VSCode terminal, run these two lines:

```
uv venv --python 3.13 --seed
uv pip install -r requirements.txt
```

The first line creates the environment (and downloads Python 3.13 if you don't have it). `--seed` also adds `pip`, so notebook cells that start with `%pip install` work on your computer too. The second line installs every package we use in the course, so you only do this once.

> **Check your `.gitignore`.** The `.venv` folder is large and should never be uploaded to GitHub. Your `.gitignore` already includes `.venv/` if you followed [Setting up Git](02-git-setup.md#4-add-a-gitignore-to-your-repository) (the Python template). After step 3, the Source Control tab should **not** list hundreds of new files. If it does, add a line `.venv/` to `.gitignore`.

---

## 4. Open a notebook and choose the environment

1. Make a folder for notebooks inside your website folder, e.g. `notebooks`.
2. Download a notebook from the course repo (e.g. [`DS3_2_Requests_Shiller.ipynb`](../weeks/week03/notebooks/DS3_2_Requests_Shiller.ipynb)) into it, using **Download raw file** as before.
3. Open the notebook in VSCode.
4. Click **Select Kernel** at the top right of the notebook → **Python Environments** → choose the one marked **.venv**.

> The kernel is the copy of Python that runs your notebook. If you pick the wrong one, you'll get `ModuleNotFoundError: No module named 'pandas'`. Choose `.venv` again.

5. Test it: add a code cell at the top, run it with **Shift + Enter**, and check it prints `ready`:

```python
import pandas, altair, requests
print("ready")
```

---

## Differences from Colab

| | Colab | Your computer |
|---|---|---|
| Where files are saved | Temporary Colab storage, so you must download them | Your folder, next to the notebook |
| `from google.colab import files` | Works | **Doesn't exist.** Skip these cells: your files are already in your folder |
| `%pip install ...` cells | Needed for some packages | Safe to run: they just check the package is installed and up to date |
| Saving your work | Save a copy in Drive | `Cmd + S` / `Ctrl + S`, then commit as usual |

**File paths:** a notebook saves files in **its own folder**. To save a CSV into a `data` folder next to `notebooks`, use `'../data/my_data.csv'` (`..` means "go up one folder").

---

## Adding a package later

If a notebook needs a package that isn't installed, install it into your environment from the VSCode terminal (in your website folder):

```
uv pip install package-name
```

Then add it to `requirements.txt`, so the list stays complete.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `uv: command not found` (Mac) or `uv is not recognized` (Windows) | Close and reopen VSCode. If it still fails, restart your computer |
| `.venv` doesn't appear in **Select Kernel** | **View → Command Palette** → `Developer: Reload Window`, then try again |
| `ModuleNotFoundError: No module named ...` | Wrong kernel (choose `.venv`), or the package isn't installed (`uv pip install ...`) |
| `No module named pip` when running a `%pip` cell | Your environment was made without `--seed`. Run `uv pip install pip` in the terminal, then try again |
| VSCode asks to install `ipykernel` | Click **Install**. It's in `requirements.txt`, so this usually means the wrong kernel is selected |
| Source Control shows hundreds of new files | `.venv` isn't ignored: add `.venv/` to `.gitignore` |
| Strange errors about files being in use or missing | Is your folder inside OneDrive, iCloud or Dropbox? Move it to your `code` folder (see [Setting up Git](02-git-setup.md#5-choose-where-your-code-will-live)) |
