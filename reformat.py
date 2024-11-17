import pandas as pd

# Assuming the CSV data is in a file named 'ao3_data.csv' with the columns:
# Year, Pairing, Fandom, Type, Race, Works

# Read the CSV file
df = pd.read_csv('AO3 Stats.csv')

# Group by Fandom and aggregate Works
df_grouped = df.groupby('Fandom')['Works'].apply(list).reset_index()

# Convert the list of works into a comma-separated string
df_grouped['Works'] = df_grouped['Works'].apply(lambda x: ', '.join(map(str, x)))

# Print the DataFrame
print(df_grouped)

# Save the DataFrame to a CSV file
df_grouped.to_csv('fandom_works.csv', index=False)