import json
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_random_datetime(start_date, end_date):
    """
    Generate a random datetime between start_date and end_date.
    
    :param start_date: The start date as a datetime object.
    :param end_date: The end date as a datetime object.
    :return: A random datetime object between the start and end dates.
    """
    time_difference = end_date - start_date
    random_seconds = random.randint(0, int(time_difference.total_seconds()))
    random_datetime = start_date + timedelta(seconds=random_seconds)
    return random_datetime

# Define the start and end dates
start_date = datetime(2022, 1, 1)
end_date = datetime.now()

def generate_user_event():
    # Generate a random datetime for the eventTime
    random_event_time = generate_random_datetime(start_date, end_date).isoformat() + "Z"
    
    return {
        "eventType": random.choice(["home-page-view"]),
        "visitorId": uuid.uuid4().hex,
        "sessionId": uuid.uuid4().hex,
        "eventTime": random_event_time,
        "experimentIds": [fake.word() for _ in range(random.randint(1, 3))],
        "attributionToken": fake.sha256(),
        "attributes": {
            fake.word(): {
                "text": [fake.word(), fake.word()],
                "searchable": fake.boolean(),
                "indexable": fake.boolean()
            }
        }
    }

user_events = [generate_user_event() for _ in range(1000)]

# Write the events to a file, one JSON object per line
with open('userEvents-homepage.json', 'w') as f:
    for event in user_events:
        f.write(json.dumps(event) + '\n')
