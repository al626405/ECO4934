import pandas as pd

# Step 1: Read the original CSV file
file_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/bug_status.csv'
df = pd.read_csv(file_path)

# Step 2: Drop the first column (assuming it's unnamed or you know its name)
df.drop(df.columns[0], axis=1, inplace=True)

# Step 3: Save the modified DataFrame to a new CSV file
output_file_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/bug_status_final.csv'
df.to_csv(output_file_path, index=False)

print(f"Modified CSV saved to {output_file_path}")
