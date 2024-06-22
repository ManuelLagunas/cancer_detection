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
