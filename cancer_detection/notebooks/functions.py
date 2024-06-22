# ==========Libraries ==========

import os
import pandas as pd
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
    import os
    import pandas as pd

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
