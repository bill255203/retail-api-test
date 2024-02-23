import json
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker
from random import randint

fake = Faker()
def generate_random_datetime(start_date, end_date):
    time_difference = end_date - start_date
    random_seconds = random.randint(0, int(time_difference.total_seconds()))
    return start_date + timedelta(seconds=random_seconds)
def generate_fake_product():
    product_id = uuid.uuid4().hex
    return {
        "id": product_id,
        "title": f"{fake.word().capitalize()} sneakers",
        "description": "High-quality sneakers for every occasion.",
        "categories": [f"Category {random.randint(1, 10)}"],
        "attributes": {"vendor": {"text": [f"vendor{random.randint(100, 999)}"]}},
        "language_code": "en",
        "tags": [f"Tag{random.randint(1, 5)}"],
        "priceInfo": {
            "currencyCode": "USD",
            "price": random.randint(50, 150),
            "originalPrice": random.randint(150, 300),
            "cost": random.randint(20, 49)
        },
        "availableQuantity": random.randint(10, 100),
        "uri": fake.url(),
        "images": [{"uri": fake.image_url(), "height": 320, "width": 320}]
    }


# Step 1: Generate and write product catalog
# with open('products.json', 'w') as f:
#     for _ in range(10000):
#         product = generate_fake_product()
#         f.write(json.dumps(product) + '\n')

# Step 2: Read the product catalog back into the script
products = []
with open('products.json', 'r') as f:
    products = [json.loads(line) for line in f]

def generate_user_event_sequences(visitor_id, products, num_sequences):
    events = []
    for _ in range(num_sequences):
        product = random.choice(products)
        event_time = generate_random_datetime(datetime(2022, 1, 1), datetime.now())
        # Simplify by using a single product per user sequence for clarity
        events.append({
            "eventType": "search",
            "visitorId": visitor_id,
            "eventTime": event_time.isoformat() + "Z",
            "searchQuery": fake.sentence()
        })
        # Increment event time for sequential actions
        event_time += timedelta(days=randint(1,10))
        events.append({
            "eventType": "detail-page-view",
            "visitorId": visitor_id,
            "eventTime": event_time.isoformat() + "Z",
            "productDetails": [{"product": {"id": product["id"]}, "quantity": 1}]
        })
        event_time += timedelta(days=randint(1,10))
        events.append({
            "eventType": "add-to-cart",
            "visitorId": visitor_id,
            "eventTime": event_time.isoformat() + "Z",
            "productDetails": [{"product": {"id": product["id"]}, "quantity": 1}]
        })
        event_time += timedelta(days=randint(1,10))
        events.append({
            "eventType": "purchase-complete",
            "visitorId": visitor_id,
            "eventTime": event_time.isoformat() + "Z",
            "productDetails": [{"product": {"id": product["id"]}, "quantity": 1}],
            "purchaseTransaction": {"revenue": product["priceInfo"]["price"], "currencyCode": "USD"}
        })
    return events

num_users = 2500  # Adjust number of users
num_sequences_per_user = 3  # Number of event sequences per user

user_events = []
for _ in range(num_users):
    visitor_id = uuid.uuid4().hex
    user_events += generate_user_event_sequences(visitor_id, products, num_sequences_per_user)

# Write user events, ensuring not to exceed 30,000 events
with open('userEvents.json', 'w') as f:
    for event in user_events[:30000]:  # Adjust as needed based on event count
        f.write(json.dumps(event) + '\n')