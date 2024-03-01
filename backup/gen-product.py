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

with open('products.json', 'w') as f:
    for _ in range(10000):
        product = generate_fake_product()
        f.write(json.dumps(product) + '\n')