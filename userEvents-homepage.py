import json
import random
import uuid
from datetime import datetime
from faker import Faker

fake = Faker()

def generate_user_event():
    return {
        "eventType": random.choice(["home-page-view"]),
        "visitorId": uuid.uuid4().hex,
        "sessionId": uuid.uuid4().hex,
        "eventTime": datetime.now().isoformat() + "Z",
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

user_events = [generate_user_event() for _ in range(10)]

# Open the file in write mode
with open('userEvents.json', 'w') as f:
    # Iterate over each user event
    for event in user_events:
        # Convert the event to a JSON string and write it to the file followed by a newline
        f.write(json.dumps(event) + '\n')
