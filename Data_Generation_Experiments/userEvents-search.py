import json
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_random_datetime(start_date, end_date):
    """
    Generate a random datetime between start_date and end_date.
    
    :param start_date: The start date as a datetime object (e.g., datetime(2022, 1, 1)).
    :param end_date: The end date as a datetime object (e.g., datetime.now()).
    :return: A random datetime object between the start and end dates.
    """
    time_difference = end_date - start_date
    random_seconds = random.randint(0, int(time_difference.total_seconds()))
    return start_date + timedelta(seconds=random_seconds)

def generate_search_user_event():
    event_datetime = generate_random_datetime(datetime(2022, 1, 1), datetime.now()).isoformat() + "Z"
    search_query = fake.sentence(nb_words=6)  # Generate a fake search query
    
    return {
        "eventType": "search",
        "visitorId": uuid.uuid4().hex,
        "sessionId": uuid.uuid4().hex,
        "eventTime": event_datetime,
        "searchQuery": search_query,  # Required for search events
        "experimentIds": [fake.word() for _ in range(random.randint(1, 3))],
        "attributionToken": fake.sha256(),
        "attributes": {
            fake.word(): {
                "text": [fake.word(), fake.word()],
                "searchable": fake.boolean(),
                "indexable": fake.boolean()
            }
        }
        # Note: The document provided specifies additional fields that may be required for other types of events
        # or for more detailed search events. Adjust and add fields as necessary for your testing needs.
    }

# Generate 10 fake search user events
user_events = [generate_search_user_event() for _ in range(1000)]

# Write the events to a file, one JSON object per line
with open('userEvents-search.json', 'w') as f:
    for event in user_events:
        f.write(json.dumps(event) + '\n')
