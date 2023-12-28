import pandas as pd

# Replace 'your_file.csv' with the actual name of your CSV file
file_path = '/home/user/Desktop/Data Analytics Project/Fetched_data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Remove last row
df.drop(df.index[-1], inplace=True)

# Replace null values with zero for all columns
df.fillna(0, inplace=True)

# Save the modified DataFrame to a new CSV file
output_file_path = '/home/user/Desktop/Data Analytics Project/final_data.csv'
df.to_csv(output_file_path, index=False)

# Print the DataFrame to verify the changes
print(df)
print(output_file_path, "file created successfully.")