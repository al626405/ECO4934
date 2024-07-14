import pandas as pd

# Define file path
cc_cleaned_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/cc_cleaned.csv'

# Load the CSV file into a pandas dataframe
df_cc_cleaned = pd.read_csv(cc_cleaned_file)

# Extract the unique IDs from the first column (assuming the first column is 'id')
unique_ids = df_cc_cleaned.iloc[:, 0].unique()

# Count the number of unique IDs
num_unique_ids = len(unique_ids)

print(f"The number of unique IDs in {cc_cleaned_file} is {num_unique_ids}")
