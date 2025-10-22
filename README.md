# Mechanical_Engineering_python

**Mechanical_Engineering_python** is a Python package designed to help mechanical engineering students learn Python programming through interactive Jupyter notebooks. Once installed, it allows you to run bundled course notebooks directly from the command line.written by vahid ahmadi khorami.

---

## 🚀 Features

* Execute a full Jupyter Notebook directly from the terminal.
* Clean, colorful output using the `rich` library.
* Handles errors gracefully while showing all results and logs.
* Compatible with Windows, macOS, and Linux.
* Ideal for teaching environments and classroom demos.

---

## 📦 Installation

You can install it directly from GitHub:

```bash
pip install git+https://github.com/vahid2510/Book.git
```

Or clone the repository and install manually:

```bash
git clone https://github.com/vahid2510/Book.git
cd Mechanical_Engineering_python
pip install -e .
```

---

## ▶️ Usage

Once installed, you can run the course notebook from anywhere using:

```bash
mech-eng
```

### Options

```bash
mech-eng --nb notebooks/course.ipynb   # specify a notebook path
mech-eng --timeout 300                 # change cell execution timeout (seconds)
```

For example:

```bash
mech-eng --nb notebooks/lesson1.ipynb --timeout 600
```

The tool will execute all cells in the given notebook and display outputs in your terminal using formatted panels.

---

## 🧠 How It Works

Internally, the package uses:

* **nbformat** to read the Jupyter notebook structure.
* **nbclient** to execute notebook cells programmatically.
* **rich** for colorful, styled output panels in the terminal.

Errors, results, and text outputs are all captured and displayed neatly. Non-text outputs (like images or plots) will be indicated but not rendered in the terminal.

---

## 🧩 Folder Structure

```
Book/
├── pyproject.toml
├── README.md
├── LICENSE
└── src/
    └── Mechanical_Engineering_python/
        ├── __init__.py
        ├── cli.py
        └── notebooks/
            └── course.ipynb
```


---

## 🧰 Dependencies

All required libraries are included in the package:

* `nbformat`
* `nbclient`
* `rich`
* `numpy`
* `sympy`
* `matplotlib`
* `scipy`
* `pint`

These ensure your notebooks run smoothly without additional setup.

---

## 💡 Example Output

When you run `mech-eng`, you'll see something like this:

```
─────────────────────────────
Running notebook: notebooks/course.ipynb
─────────────────────────────

┌──────────────────────────────────────┐
│ Hello from the course notebook!      │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ Solve Ax=b: [4. 5.]                  │
└──────────────────────────────────────┘

✔ Done.
```

---

## 🧭 Development Guide

If you want to modify or extend the package:

1. Clone the repo.
2. Add or update notebooks under `src/Mechanical_Engineering_python/notebooks/`.
3. Edit `cli.py` to customize notebook execution or output style.
4. Test locally:

   ```bash
   python -m Mechanical_Engineering_python.cli
   ```
5. Commit and push to GitHub.

---

## 📘 License

This project is licensed under the **MIT License**. Feel free to modify and distribute it for educational use.

---

## 👨‍🏫 Credits

Developed as a teaching aid for Mechanical Engineering students learning Python programming. The package aims to bridge theoretical learning with hands-on programming practice.

---

### 🧩 Example GitHub Button for Binder

You can make your notebooks run online via [MyBinder](https://mybinder.org):

```markdown
vahid2510/Book/main?labpath=src/Mechanical_Engineering_python/notebooks/course.ipynb
```

Clicking the badge will open your notebook interactively online.

---

## 🏁 Summary

| Command     | Description                      |
| ----------- | -------------------------------- |
| `mech-eng`  | Run the default bundled notebook |
| `--nb`      | Select which notebook to run     |
| `--timeout` | Adjust execution time per cell   |

This package makes learning Python for Mechanical Engineering smoother, faster, and more interactive.
