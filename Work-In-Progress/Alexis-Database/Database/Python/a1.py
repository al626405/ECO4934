import pandas as pd
import glob

# Path to the directory containing all CSV files
folder_path = '/home/Alexis/Courses/Eco4934/Final Project/Case/'

# Path to cc.csv and other CSV files
cc_path = folder_path + 'cc.csv'
eclipse_files_pattern = folder_path + 'Eclipse/*.csv'

# Function to load and correct cc.csv based on a reference
def correct_cc_csv(cc_path, reference_paths):
    # Load reference CSV files
    reference_dataframes = []
    for file_path in reference_paths:
        df = pd.read_csv(file_path)
        reference_dataframes.append(df)
    
    # Load cc.csv with error handling
    try:
        cc_df = pd.read_csv(cc_path, error_bad_lines=False)
    except pd.errors.ParserError as e:
        print(f"Error parsing {cc_path}: {e}")
        return
    
    # Correct cc.csv based on references
    for ref_df in reference_dataframes:
        # Compare columns to find the correct structure
        if cc_df.columns.tolist() == ref_df.columns.tolist():
            # Assume this is the correct structure
            correct_columns = ref_df.columns.tolist()
            break
    
    # Ensure cc_df has the correct structure
    cc_df = cc_df[correct_columns]
    
    # Remove duplicate rows
    cc_df = cc_df.drop_duplicates()
    
    # Remove rows with missing values
    cc_df = cc_df.dropna()
    
    # Save corrected cc.csv
    cc_df.to_csv(cc_path, index=False)
    print(f"Successfully corrected and cleaned {cc_path}")

# Get list of reference CSV files
reference_paths = glob.glob(eclipse_files_pattern)

# Correct and clean cc.csv based on references
correct_cc_csv(cc_path, reference_paths)
