# ML Beginner Starter Pack

Three small, self-contained machine-learning projects for beginners. Every
dataset is included, so you can run each notebook top to bottom without
downloading or uploading anything.

## What's inside

```
Machine-Learning/
├── README.md                 <- you are here
├── requirements.txt          <- Python packages needed
├── setup_data.py             <- optional: regenerates the CSV files
├── data/
│   ├── iris.csv              <- 150 flowers, 4 features + species
│   ├── digits.csv            <- 1,797 handwritten digits (8x8 pixels)
│   └── landpriceprediction.csv <- 10 land plots (size -> price)
└── Projects/
    ├── 01/
    │   └── 01_leaf_species_detection.ipynb
    ├── 02/
    │   └── 02_handwritten_digit_recognition_svm.ipynb
    └── 03/
        └── 03_land_price_prediction.ipynb
```

## The three projects

| # | Notebook | Task | Model | Type |
|---|----------|------|-------|------|
| 1 | `01_leaf_species_detection.ipynb` | Classify iris flowers into 3 species | Decision Tree | Classification |
| 2 | `02_handwritten_digit_recognition_svm.ipynb` | Recognise digits 0-9 from images | SVM | Classification |
| 3 | `03_land_price_prediction.ipynb` | Predict land price from its size | Linear Regression | Regression |

Each notebook follows the same simple flow: **load -> explore -> split -> train
-> predict -> evaluate**, with short explanations between the code cells.

## Datasets

All three live in the `data/` folder and are referenced from the notebooks with
a **relative path** (for example `../../data/iris.csv`), so the pack keeps working
wherever you move it.

- `iris.csv` - the classic Iris dataset, built into scikit-learn.
- `digits.csv` - 8x8 handwritten digits, built into scikit-learn.
- `landpriceprediction.csv` - a tiny toy table for learning regression.

## How to run

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```

2. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Start Jupyter from inside the pack folder:

   ```bash
   jupyter lab
   ```

4. Open a notebook from its numbered folder inside `Projects/` (`01/`, `02/`, or `03/`) and run all cells.

## Using Google Colab

Upload the whole `ML_Beginner_Starter` folder to Colab (or a Drive folder), keep
the `Projects/` and `data/` folders side by side, open a notebook and run all
cells. The relative paths will resolve on their own.

## Rebuilding the data (optional)

The CSV files are already included, so this step is not needed. If you delete
them and want them back, run:

```bash
python setup_data.py
```
