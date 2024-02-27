import pandas as pd
import json

# Load the CSV data into a DataFrame
csv_data = pd.read_csv('techorange-postmeta-20240206.csv')  # The CSV file is named 'orange.csv'

# Function to convert each row to a JSON object
def map_row_to_json(row):
    # Convert categories and tags to strings if they are not NaN, otherwise set as empty lists
    categories = str(row['categories']).strip("[]").split(", ") if pd.notna(row['categories']) else []
    tags = str(row['tags']).strip("[]").split(", ") if pd.notna(row['tags']) else []
    
    return {
        "title": row['title'],
        "id": str(row['ID']),
        "publishTime": row['date'],
        "categories": categories, 
        "tags": tags,
    }

# Create a list of JSON objects
json_data = [map_row_to_json(row) for index, row in csv_data.iterrows()]

# Write each JSON object to a file, one object per line
with open('output.json', 'w', encoding='utf-8') as f:
    for item in json_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
