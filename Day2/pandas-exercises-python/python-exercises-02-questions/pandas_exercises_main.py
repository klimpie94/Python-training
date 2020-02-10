
import os
from pathlib import Path

from utils.transformation_functions import (
    read_csv_files, filter_films, join_categories_with_metadata,
    categories_into_one_single_column, take_year_from_movie_title_string,
    calculate_ratio_of_nomination_over_win,
    genre_count_table_for_movies_with_aggregation)


DATA_PATH = os.path.join(
    os.fspath(Path(__file__).parents[0]),
    "data")

IMDB_CATEGORY_PATH = os.path.join(DATA_PATH, "imdb_category_binary.csv")
IMDB_FACTS_PATH = os.path.join(DATA_PATH, "imdb_facts.csv")
EXERCISE_OUTPUT_PATH = os.path.join(DATA_PATH, "analysis.csv")


if __name__ == "__main__":

    print("No implementation")
