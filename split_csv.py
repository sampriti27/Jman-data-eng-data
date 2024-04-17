import pandas as pd
import os

def split_csv_evenly(file_path, num_files):
    print("Splitting CSV file...")
    # Read the original CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, skiprows=3, encoding='latin-1')

    # Calculate the number of rows per file
    rows_per_file = len(df) // num_files
    remainder_rows = len(df) % num_files

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Split the DataFrame into chunks and write to separate CSV files
    start_idx = 0
    for i in range(num_files):
        end_idx = start_idx + rows_per_file + (1 if i < remainder_rows else 0)
        subset_df = df.iloc[start_idx:end_idx]
        subset_df.to_csv(os.path.join(output_dir, f"output_{i+1}.csv"), index=False)
        start_idx = end_idx
        print(f"File {i+1} created with {len(subset_df)} rows.")

# Specify the file path and the number of files to split into
file_path = r"E:\JmanDataEngineering\merge-csv.com__661d607bdd5aa.csv"
num_files = 3

# Call the function to split the CSV file evenly
split_csv_evenly(file_path, num_files)
