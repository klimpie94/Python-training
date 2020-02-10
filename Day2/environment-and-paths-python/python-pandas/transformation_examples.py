import pandas as pd


# Reading files
crime_df = pd.read_csv("./python-pandas/dataset_boston/crime.csv",
                       encoding="latin-1")
offense_codes = pd.read_csv("./python-pandas/dataset_boston/offense_codes.csv",
                            encoding="latin-1")

# Displaying rows
print(crime_df.head())

print(offense_codes.head())

# # Displaying column names
print(crime_df.columns)

# Displaying data types for each column
print(crime_df.dtypes)

# Changing column names
crime_df.columns = [col.lower() for col in crime_df.columns]

print(crime_df.columns)

# LOC versus ILOC
print(crime_df.loc[:, ["street", "lat", "long"]])
print(crime_df.iloc[:, 1:3])

# Filtering rows based on column values
print(crime_df.loc[crime_df.offense_code == 1402, :].head())
print(crime_df.loc[crime_df.offense_code.isin([1402, 111])])

# Merging dataframes
merged_df = pd.merge(left=crime_df, right=offense_codes,
                     left_on="offense_code", right_on="CODE")
# print(merged_df.head(100))


# Some more dataset properties
filtered_df = merged_df.loc[:,
                            ["incident_number",
                             "NAME",
                             "occurred_on_date",
                             "shooting",
                             "offense_code",
                             "lat",
                             "long"]]

print(filtered_df.head(100))

print(filtered_df.isnull().sum())

print(filtered_df.shape)

# Apply function to get more general offense types
# DRUGS
# ASSAULT
# LARCENY
# ACCIDENT
# OTHERS
print(filtered_df.NAME.unique())


def change_the_offense_name(row):
    if "DRUGS" in row:
        return "DRUGS"
    elif "ASSAULT" in row:
        return "ASSAULT"
    elif "LARCENY" in row:
        return "LARCENY"
    elif "ACCIDENT" in row:
        return "ACCIDENT"
    return "OTHERS"


filtered_df["offense_name_categorical"] = filtered_df.NAME.apply(
    change_the_offense_name)


print(filtered_df.head())

# Export dataset
filtered_df.to_csv(
    "./python-pandas/exported_dataset/filtered_dataset.csv",
    sep=",",
    index=False)
