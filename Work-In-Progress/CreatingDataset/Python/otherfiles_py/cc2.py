import pandas as pd

# Define the path to your cc_cleaned.csv file
cc_cleaned_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/cc_cleaned.csv'

# Load the CSV file into a pandas DataFrame
df_cc_cleaned = pd.read_csv(cc_cleaned_file)

# Aggregate emails for each report_id
df_agg = df_cc_cleaned.groupby('report_id').agg({
    'cc_email': lambda x: ', '.join(x),
    'when': 'first',  # Choose the first 'when' value
    'who': 'first'    # Choose the first 'who' value
}).reset_index()

# Save the aggregated data back to a new CSV file
output_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/cc_cleaned_aggregated.csv'
df_agg.to_csv(output_file, index=False)

print(f"Aggregated cc_cleaned data saved to {output_file}")
