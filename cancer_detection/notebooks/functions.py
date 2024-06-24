# ==========Libraries ==========

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ========== Loading Data ==========

#  ---------- Load last csv ----------

def load_last_csv_from_directory(directory_path):
    """
    Search the specified directory and its subdirectories to find the last CSV file.
    Load this file into a pandas DataFrame and return it.
    
    :param directory_path: Path of the directory to search for CSV files.
    :return: pandas DataFrame loaded from the last found CSV file, or None if none is found.
    """
    last_dirname = None
    last_filename = None

    # Read file name from project path
    for dirname, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith('.csv'):  # Ensure it is a CSV file
                print(os.path.join(dirname, filename))
                last_dirname = dirname
                last_filename = filename

    # Check if any file was found and create DataFrame
    if last_dirname is not None and last_filename is not None:
        df = pd.read_csv(os.path.join(last_dirname, last_filename))
        return df
    else:
        print("No CSV files found.")
        return None

# ---------- Load csvs ----------

def load_csvs_as_individual_dfs(directory_path):
    """
    Traverse all CSV files in the specified directory and its subdirectories,
    load each into a DataFrame, and return a list of DataFrames.
    
    :param directory_path: Path of the directory to search for CSV files.
    :return: List of DataFrames, each loaded from a found CSV file.
    """

    # List to store dataframes
    dfs = []

    # Traverse all CSV files in the directory and subdirectories
    for dirname, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith('.csv'):  # Ensure it is a CSV file
                file_path = os.path.join(dirname, filename)
                print(file_path)
                df = pd.read_csv(file_path)
                dfs.append(df)

    if not dfs:
        print("No CSV files found.")

    return dfs

# ========== EDA ==========

# ---------- Column features categorization ----------

def classify_columns(df):
    """
    Classifies columns of a DataFrame into binary, categorical, and continuous.

    :param df: DataFrame to classify.
    :return: A dictionary with three keys ('binary', 'categorical', 'continuous') and column names as lists.
    """
    binary_columns = []
    categorical_columns = []
    continuous_columns = []

    for column in df.columns:
        unique_values = df[column].dropna().unique()
        num_unique_values = len(unique_values)

        if num_unique_values == 2:
            binary_columns.append(column)
        elif 2 < num_unique_values < 5:  # Adjusted to include the value 4 in categorical classification
            categorical_columns.append(column)
        else:
            continuous_columns.append(column)

    return {
        'binary': binary_columns,
        'categorical': categorical_columns,
        'continuous': continuous_columns
    }

#  ---------- Binary data visualization ----------

def plot_binary_column(df, column_name, title):
    """
    Creates a bar plot for a binary column with two colors.
    
    Parameters:
    - df: pandas DataFrame containing the data.
    - column_name: Name of the binary column to plot.
    - title: Title of the plot.
    """
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        print(f"Column '{column_name}' does not exist in the DataFrame.")
        return
    
    # Count the frequency of values in the binary column
    value_counts = df[column_name].value_counts()
    
    # Create the bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=value_counts.index, y=value_counts.values, palette='coolwarm')
    plt.title(title)
    plt.xlabel('Category')
    plt.ylabel('Frequency')
    plt.xticks(ticks=[0, 1], labels=['Category 1', 'Category 2'])  # Adjust labels as needed
    plt.show()