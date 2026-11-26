import os

import pandas as pd
from sklearn.datasets import load_iris, load_digits

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
os.makedirs(DATA_DIR, exist_ok=True)

land = pd.DataFrame(
    {
        "land": [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
        "price": [2245, 4575, 6874, 8878, 10589, 12457, 14785, 16785, 18958, 20789],
    }
)
land.to_csv(os.path.join(DATA_DIR, "landpriceprediction.csv"), index=False)

iris = load_iris()
iris_df = pd.DataFrame(
    iris.data,
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"],
)
iris_df["species"] = [iris.target_names[i] for i in iris.target]
iris_df["target"] = iris.target
iris_df = iris_df[
    ["sepal_length", "sepal_width", "petal_length", "petal_width", "species", "target"]
]
iris_df.to_csv(os.path.join(DATA_DIR, "iris.csv"), index=False)

digits = load_digits()
pixel_columns = [f"pixel_{i}" for i in range(digits.data.shape[1])]
digits_df = pd.DataFrame(digits.data, columns=pixel_columns)
digits_df["label"] = digits.target
digits_df = digits_df[pixel_columns + ["label"]]
digits_df.to_csv(os.path.join(DATA_DIR, "digits.csv"), index=False)

print("Rebuilt datasets in:", DATA_DIR)
