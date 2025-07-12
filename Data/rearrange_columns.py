import pandas as pd

# Read the CSV file
df = pd.read_csv('cleaned_climate_data.csv')

# Get the current column order
current_columns = df.columns.tolist()
print("Current columns:", current_columns)

# Remove 'disease_outbreak' from its current position
columns_without_disease = [col for col in current_columns if col != 'disease_outbreak']

# Add 'disease_outbreak' as the last column
new_column_order = columns_without_disease + ['disease_outbreak']
print("New column order:", new_column_order)

# Reorder the DataFrame
df_reordered = df[new_column_order]

# Save the reordered DataFrame back to the CSV file
df_reordered.to_csv('cleaned_climate_data.csv', index=False)

print("Successfully moved 'disease_outbreak' column to the end!")
print("First few rows of the reordered data:")
print(df_reordered.head())
