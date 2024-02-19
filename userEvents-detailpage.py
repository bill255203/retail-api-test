import json
import random
import uuid
from datetime import datetime
from faker import Faker

fake = Faker()

def generate_fake_product(product_id):
    return {
        "product": {
            "id": str(product_id),
            "title": f"{fake.word().capitalize()} sneakers",
            "description": "Sneakers for the rest of us",
            "categories": ["Apparel & Accessories > Shoes"],
            "attributes": {
                "vendor": {"text": [f"vendor{fake.random_int(min=100, max=999)}"]}
            },
            "language_code": "en",
            "tags": ["black-friday"],
            "priceInfo": {
                "currencyCode": "USD",
                "price": fake.random_int(min=50, max=150),
                "originalPrice": fake.random_int(min=200, max=300),
                "cost": fake.random_int(min=20, max=49)
            },
            "availableQuantity": fake.random_int(min=1, max=100),
            "uri": fake.url(),
            "images": [
                {"uri": fake.image_url(), "height": 320, "width": 320}
            ]
        },
        "quantity": fake.random_int(min=1, max=5)
    }

def generate_user_event():
    product_id = uuid.uuid4().hex  # Generate a fake product ID
    product_details = generate_fake_product(product_id)  # Generate fake product details
    return {
        "eventType": "detail-page-view",
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
        },
        "productDetails": [product_details]  # Include the generated product details
    }

# Generate 10 fake user events with product details
user_events = [generate_user_event() for _ in range(10000)]

# Write the events to a file, one JSON object per line
with open('userEvents-detailpage.json', 'w') as f:
    for event in user_events:
        f.write(json.dumps(event) + '\n')
