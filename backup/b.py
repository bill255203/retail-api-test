import pandas as pd
import json

# Load the CSV data into a DataFrame
csv_data = pd.read_csv('techorange-pageview-202401.csv')

# Function to convert each row to a UserEvent JSON object
def map_row_to_user_event_json(row):
    # Format the event date to RFC3339 with 'Z' and nanoseconds
    event_time = pd.to_datetime(row['event_date']).tz_localize('UTC')
    event_time_rfc3339 = event_time.strftime('%Y-%m-%dT%H:%M:%S.000000000Z')
    
    # Prepare the attributes dictionary
    attributes = {}
    if pd.notna(row['param_key']):
        # Check if the value is a string or int and add to attributes accordingly
        if pd.notna(row['param_string_value']):
            attributes[row['param_key']] = row['param_string_value']
        elif pd.notna(row['param_int_value']):
            attributes[row['param_key']] = row['param_int_value']
    
    # Create the UserEvent JSON object
    user_event_json = {
        "eventType": "detail-page-view",
        "sessionId": str(row['event_bundle_sequence_id']),
        "eventTime": event_time_rfc3339,
        "visitorId": row['user_id'],
        "attributes": attributes
    }
    
    return user_event_json

# Create a list of UserEvent JSON objects
user_event_json_data = [map_row_to_user_event_json(row) for index, row in csv_data.iterrows()]

# Write each UserEvent JSON object to a file, one object per line
with open('userevents.json', 'w', encoding='utf-8') as f:
    for item in user_event_json_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
