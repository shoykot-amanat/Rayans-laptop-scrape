import pandas as pd
import re

# Read the CSV file into a DataFrame
df = pd.read_csv('updatedlaptop.csv')

# Define a function to extract numeric values from strings
def extract_numeric(s):
    numeric_part = re.search(r'\d+(?:,\d+)*', s)
    if numeric_part:
        return int(numeric_part.group().replace(',', ''))
    return None

# Apply the function to the 'price' column to extract numeric values
df['Price'] = df['Price'].apply(lambda x: extract_numeric(x))

# Filter the DataFrame to include only rows where the price is less than 55000
filtered_df = df[df['Price'] < 55000]

# Print the filtered DataFrame
print(filtered_df)

filtered_df.to_csv('filtered_laptops.csv', index=False) 

# If you want to save the filtered DataFrame back to a CSV file
# filtered_df.to_csv('filtered_laptops.csv', index=False)  # Uncomment this line if you want to save the filtered dataset

