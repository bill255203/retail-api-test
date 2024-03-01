import pandas as pd
import json

# Load the CSV data into a DataFrame
csv_data = pd.read_csv('techorange-pageview-202401.csv')

# Adjusted function to create the desired JSON structure for attributes
def map_row_to_user_event_json(row):
    # Parse the event_date assuming it's in 'YYYYMMDD' format
    event_time = pd.to_datetime(row['event_date'], format='%Y%m%d')
    # Convert to UTC and format as RFC3339 with 'Z' and nanoseconds
    event_time_rfc3339 = event_time.strftime('%Y-%m-%dT%H:%M:%S.000000000Z')param
    
    # Initialize an empty attributes dictionary
    attributes = {}
    
    if pd.notna(row['param_key']):
        # Initialize the key with empty lists for text and numbers
        if row['param_key'] not in attributes:
            attributes[row['param_key']] = {"text": [], "numbers": []}
        
        # Check if the value is a string and add to attributes accordingly
        if pd.notna(row['param_string_value']):
            # For text values
            attributes[row['param_key']]["text"].append(row['param_string_value'])
        elif pd.notna(row['param_int_value']):
            # For numeric values
            attributes[row['param_key']]["numbers"].append(row['param_int_value'])
    
    # Create the UserEvent JSON object with the new attributes structure
    user_event_json = {
        "eventType": "detail-page-view",
        "sessionId": str(row['event_bundle_sequence_id']),
        "eventTime": event_time_rfc3339,
        "visitorId": row['user_id'],
        "attributes": attributes
    }
    
    return user_event_json

# Create a list of UserEvent JSON objects with the modified structure
user_event_json_data = [map_row_to_user_event_json(row) for index, row in csv_data.iterrows()]

# Write each UserEvent JSON object to a file, one object per line
with open('userevents_modified.json', 'w', encoding='utf-8') as f:
    for item in user_event_json_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
