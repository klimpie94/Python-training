import pandas as pd

filtered_df = pd.read_csv(
    "./python-pandas/exported_dataset/filtered_dataset.csv")

print(filtered_df.head())

# Value counts general offenses
print(filtered_df.offense_name_categorical.value_counts())

# Group by and count
print(
    filtered_df.loc[:,
                    ["offense_name_categorical",
                     "NAME",
                     "incident_number"]].groupby(
                       ["offense_name_categorical", "NAME"]).count())

print(
    filtered_df.offense_name_categorical.value_counts(normalize=True))

# ...
