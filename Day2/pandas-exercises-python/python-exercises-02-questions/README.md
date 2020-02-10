## Pandas Exercises in Python

This is a folder that contains extensive Pandas examples...

To install the requirments:

```pip install -r ./requirements.txt```

Folder structure:

```
├── README.md
├── data
│   ├── imdb_category_binary.csv
│   └── imdb_facts.csv
├── pandas_exercises_main.py
├── preparing_dataset
├── requirements.txt
└── utils
    └── transformation_functions.py
```

Use `pandas_exercises_main.py` to call `utils.transformation_functions.py` if you prefer to use a main function to test your code.

The questions cover following:

1. Use a function to read both datasets. (hint: basic read_csv is not going to work)​

2. Use a function to filter only the video.movies. ​

3. Join both datasets using film ids. (hint: id columns are not matching – splitting might help)​

4. Categories are dummy variables. We can combine all those dummy variables into one single string column. (hint: When you use dataframe.idxmax(axis=1) you automatically create a pd.Series with categorical values as strings.)​

5. Create a year column, by using movie titles. (hint: use apply functions and try catch might be helpful while parsing the movie title string)​

6. Create an analysis table, showing the count per genre in the dataset.​

7. Create a new column, showing the ratio of win over nomination. (hint: use apply functions for multiple columns and create an additional ratio function for applying. - to find the total amount of nominations you add the number of wins as well)
