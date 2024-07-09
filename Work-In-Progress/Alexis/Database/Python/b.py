import pandas as pd
import glob

# Path to the directory containing all CSV files
folder_path = '/home/Alexis/Courses/Eco4934/Final Project/Case/'

# Path to cc_corrected.csv and other CSV files in Eclipse folder
cc_corrected_path = folder_path + 'cc_corrected.csv'
eclipse_files_pattern = folder_path + 'Eclipse/*.csv'

# Function to compare cc_corrected.csv with Eclipse/*.csv files
def compare_with_eclipse_files(cc_corrected_path, eclipse_files_pattern):
    # Load cc_corrected.csv
    try:
        cc_corrected_df = pd.read_csv(cc_corrected_path)
    except pd.errors.ParserError as e:
        print(f"Error parsing {cc_corrected_path}: {e}")
        return
    
    # Get list of reference CSV files in Eclipse folder
    reference_paths = glob.glob(eclipse_files_pattern)
    
    # Compare each reference file with cc_corrected.csv
    for file_path in reference_paths:
        try:
            ref_df = pd.read_csv(file_path)
        except pd.errors.ParserError as e:
            print(f"Error parsing {file_path}: {e}")
            continue
        
        # Check if column names match
        if not cc_corrected_df.columns.equals(ref_df.columns):
            print(f"Column mismatch found in {file_path}.")
            print(f"cc_corrected.csv columns: {cc_corrected_df.columns.tolist()}")
            print(f"{file_path} columns: {ref_df.columns.tolist()}")
            continue
        
        # Check if rows match
        if not cc_corrected_df.equals(ref_df):
            print(f"Data mismatch found in {file_path}. Differences:")
            diff_df = ref_df.compare(cc_corrected_df)
            print(diff_df)
        else:
            print(f"{file_path} matches cc_corrected.csv.")
        
        print("---")
    
    print("Comparison complete.")

# Compare cc_corrected.csv with Eclipse/*.csv files
compare_with_eclipse_files(cc_corrected_path, eclipse_files_pattern)
