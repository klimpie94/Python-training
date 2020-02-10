import pandas as pd
import os
from pathlib import Path

import warnings
warnings.filterwarnings('ignore')


DATA_PATH = os.path.join(
    os.fspath(Path(__file__).parents[1]),
    "data")
IMDB_DATA_PATH = os.path.join(DATA_PATH, "imdb_category.csv")
EXPORT_PATH = os.path.join(DATA_PATH, "imdb_category_binary.csv")


categories_df = pd.read_csv(IMDB_DATA_PATH)
cols_category = categories_df.iloc[:, 1:29].columns
categories_df_tmp = categories_df.copy(deep=True)
categories_df_tmp["film_category"] = (categories_df_tmp
                                      .loc[:, cols_category]
                                      .idxmax(axis=1)
                                      .values)

columns_to_drop = [col
                   for idx, col in enumerate(categories_df_tmp.columns)
                   if idx in range(1, 29)]
categories_df_tmp.drop(columns_to_drop, axis=1, inplace=True)

categories_binary = categories_df_tmp.join(
    pd.get_dummies(
        data=categories_df_tmp.film_category,
        prefix=None))

categories_binary.drop("film_category", axis=1, inplace=True)

categories_binary.to_csv(EXPORT_PATH, sep=",", index=False)
