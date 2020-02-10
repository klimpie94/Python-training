
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

    facts_df = read_csv_files(IMDB_FACTS_PATH)
    categories_df = read_csv_files(IMDB_CATEGORY_PATH)

    categories_with_ids = categories_into_one_single_column(categories_df)

    joined_movie_df = join_categories_with_metadata(
        facts_df, categories_with_ids)

    films_filtered = filter_films(joined_movie_df)

    films_filtered["year_int"] = facts_df.title.apply(
        take_year_from_movie_title_string)

    films_filtered["win_ratio"] = calculate_ratio_of_nomination_over_win(
        films_filtered)

    genre_count_table_for_movies_with_aggregation(
        categories_df).to_csv(
            EXERCISE_OUTPUT_PATH, index=False)
