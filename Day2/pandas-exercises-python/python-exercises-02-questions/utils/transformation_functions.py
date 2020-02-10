
import pandas as pd


def read_csv_files(file_path):
    return pd.read_csv(file_path)


def filter_films(dataframe):
    pass


def join_categories_with_metadata(facts_df, categories_df):
    # Hint: You can use lambda functions to change the id column in order to
    # use join method in pandas.
    pass


def categories_into_one_single_column(categories_df):
    # Hint: When you use dataframe.idxmax(axis=1) you automatically
    # create a pd.Series with categorical values as strings.
    pass


def take_year_from_movie_title_string(movie_title_str):
    try:
        pass
    except (IndexError, ValueError):
        return 9999


def genre_count_table_for_movies_with_aggregation(categories_df):
    pass


def calculate_ratio_of_nomination_over_win(dataframe):
    # Hint 1: Use an additional function for handling
    # zero division error.
    # Hint 2: Nominations + Wins = Total Number of Nominations

    pass
