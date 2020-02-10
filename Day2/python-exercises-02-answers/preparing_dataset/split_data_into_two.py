import os
from pathlib import Path
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


DATA_PATH = os.path.join(
    os.fspath(Path(__file__).parents[1]),
    "data")

IMDB_DATA_PATH = os.path.join(DATA_PATH, "imdb.csv")
IMDB_CATEGORY_PATH = os.path.join(DATA_PATH, "imdb_category.csv")
IMDB_FACTS_PATH = os.path.join(DATA_PATH, "imdb_facts.csv")


if __name__ == "__main__":

    imdb_df = pd.read_csv(IMDB_DATA_PATH, sep=",", escapechar="\\")

    imdb_df_reset = imdb_df.rename_axis("film_id").reset_index()

    imdb_df_reset_category = imdb_df_reset.iloc[
        :, [0] + [x for x in range(17, 45)]]

    imdb_df_reset_metadata = imdb_df_reset.iloc[
        :, [x for x in range(0, 17)]]

    del imdb_df_reset_metadata["year"]

    imdb_df_reset_category["film_id"] = (imdb_df_reset_category
                                         .film_id
                                         .apply(lambda row: f"f_{row}"))
    imdb_df_reset_metadata["film_id"] = (imdb_df_reset_metadata
                                         .film_id
                                         .apply(lambda row: f"film_{row}"))

    imdb_df_reset_category.to_csv(
        IMDB_CATEGORY_PATH, sep=",", escapechar="\\", index=False)
    imdb_df_reset_metadata.to_csv(
        IMDB_FACTS_PATH, sep=",", escapechar="\\", index=False)
