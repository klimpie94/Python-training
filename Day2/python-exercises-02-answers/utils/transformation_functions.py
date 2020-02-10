
import pandas as pd


def read_csv_files(file_path):
    return pd.read_csv(file_path, sep=",", escapechar="\\")


def filter_films(dataframe):
    return dataframe.loc[dataframe.type == "video.movie", :]


def join_categories_with_metadata(facts_df, categories_df):
    # Hint: You can use lambda functions to change the id column in order to
    # use join method in pandas.
    transform_film_id = lambda film_id: "f_" + film_id.split("_")[1]
    categories_tmp = categories_df.copy(deep=True)
    facts_tmp = facts_df.copy(deep=True)
    categories_tmp["film_id"] = categories_tmp.film_id.apply(transform_film_id)
    facts_tmp["film_id"] = facts_tmp.film_id.apply(transform_film_id)
    return pd.merge(categories_tmp, facts_tmp, how="inner", on="film_id")


def categories_into_one_single_column(categories_df):
    # Hint: When you use dataframe.idxmax(axis=1) you automatically
    # create a pd.Series with categorical values as strings.
    categories_df_tmp = categories_df.copy(deep=True)
    cols_category = categories_df.iloc[:, 1:29].columns
    categories_df_tmp["film_category"] = (categories_df_tmp
                                          .loc[:, cols_category]
                                          .idxmax(axis=1)
                                          .values)
    return categories_df_tmp.drop(cols_category, axis=1)


def take_year_from_movie_title_string(movie_title_str):
    try:
        year_as_str = (movie_title_str
                       .split(" ")[-1]
                       .replace("(", "")
                       .replace(")", ""))
        return int(year_as_str)
    except (IndexError, ValueError):
        return 9999


def genre_count_table_for_movies_with_aggregation(categories_df):
    cols_category = categories_df.iloc[:, 1:29].columns
    categories_count = categories_df.loc[:, cols_category].sum().reset_index()
    categories_count.columns = ["genre", "frequency"]
    return categories_count


def calculate_ratio_of_nomination_over_win(dataframe):
    def take_ratio_in(x, y):
        try:
            return x / (x + y)
        except ZeroDivisionError:
            return 0

    return dataframe.apply(
        lambda row: take_ratio_in(
            row["nrOfWins"], row["nrOfNominations"]), axis=1)
