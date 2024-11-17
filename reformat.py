import pandas as pd

# Load the uploaded CSV file
file_path = 'AO3 Stats.csv'
data = pd.read_csv(file_path)

# Create a new DataFrame for the output
output_data = []

# Define the years range
years = range(2013, 2025)

# Get a list of unique fandoms
fandoms = data['Fandom'].unique()

# Process each fandom
for fandom in fandoms:
    fandom_data = []
    filtered_data = data[data['Fandom'] == fandom]
    for year in years:
        yearly_data = filtered_data[filtered_data['Year'] == year]
        if not yearly_data.empty:
            max_works = yearly_data['Works'].max()
        else:
            max_works = 0
        fandom_data.append(max_works)
    output_data.append(fandom_data)

for datum in output_data:
    datum[5] = (datum[4] + datum[6]) // 2 if datum[6] != 0 else 0
    
# Create the resulting DataFrame
result_df = pd.DataFrame(output_data, columns=[str(year) for year in years], index=fandoms)

# Save to a new CSV file
result_df.to_csv('fandom_works.csv')

# Print the resulting DataFrame
print(result_df)