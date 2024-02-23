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
    random_datetime = start_date + timedelta(seconds=random_seconds)
    return random_datetime.isoformat() + "Z"

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
    
    # Define the start and end dates
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    
    # Generate a random datetime between the start and end dates for the eventTime
    event_time = generate_random_datetime(start_date, end_date)
    
    return {
        "eventType": "detail-page-view",
        "visitorId": uuid.uuid4().hex,
        "sessionId": uuid.uuid4().hex,
        "eventTime": event_time,
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

# Generate 10,000 fake user events with product details
user_events = [generate_user_event() for _ in range(2000)]

# Write the events to a file, one JSON object per line
with open('userEvents-detailpage.json', 'w') as f:
    for event in user_events:
        f.write(json.dumps(event) + '\n')
