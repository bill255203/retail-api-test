import json
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def load_product_data():
    products = []
    with open('products.json', 'r') as file:
        for line in file:
            products.append(json.loads(line))
    return products
products = load_product_data()  # Load product data once

def generate_random_datetime(start_date, end_date):
    time_difference = end_date - start_date
    random_seconds = random.randint(0, int(time_difference.total_seconds()))
    random_datetime = start_date + timedelta(seconds=random_seconds)
    return random_datetime

def generate_user_event():
    product = random.choice(products)  # Randomly select a product
    visitor_id = uuid.uuid4().hex  # Generate a fake visitor ID
    
    # Define the start and end dates
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    
    # Generate a random datetime between the start and end dates for the eventTime
    event_time = generate_random_datetime(start_date, end_date)
    
    return {
        "eventType": "detail-page-view",
        "visitorId": visitor_id,
        "eventTime": event_time.isoformat() + "Z",
        "productDetails": [{"product": {"id": product["id"]}, "quantity": random.randint(1, 15)}]
    }

# Generate 9,000 fake user events with product details
user_events = [generate_user_event() for _ in range(9000)]

# Write the events to a file, one JSON object per line
with open('userEvents-detailpage.json', 'w') as f:
    for event in user_events:
        f.write(json.dumps(event) + '\n')
