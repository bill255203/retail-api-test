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

with open('fake_user_events.json', 'w') as f:
    json.dump(user_events, f, indent=2)
