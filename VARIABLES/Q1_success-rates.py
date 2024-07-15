import pandas as pd

# Load Q1-Data_with_success_rate.csv into a DataFrame
q1_data_df = pd.read_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1-Data_with_success_rate.csv")

# Select columns 'assigned_to' and 'success_rate'
success_rate_df = q1_data_df[['assigned_to', 'success_rate']]

# Drop duplicates based on 'assigned_to'
success_rate_unique_df = success_rate_df.drop_duplicates(subset=['assigned_to'])

# Save to SuccessRate.csv
success_rate_unique_df.to_csv("/home/Alexis/Database/Python/calculatedstatistics/SuccessRate.csv", index=False)

print("SuccessRate.csv saved successfully.")
