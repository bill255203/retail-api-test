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
start_date = datetime(2024, 1, 1)
end_date = datetime.now()

# Generate a random datetime between the start and end dates
random_datetime = generate_random_datetime(start_date, end_date)


# Generate a single fake product
def generate_fake_product(product_id, index):
    price = fake.random_int(min=50, max=150)
    cost = fake.random_int(min=20, max=49)
    return {
        "name": f"projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/{index}",
        "id": str(product_id),
        "categories": ["Apparel & Accessories > Shoes"],
        "title": f"{fake.word().capitalize()} sneakers",
        "description": "Sneakers for the rest of us",
        "attributes": {"vendor": {"text": [f"vendor{fake.random_int(min=100, max=999)}", f"vendor{fake.random_int(min=100, max=999)}"]}},
        "language_code": "en",
        "tags": ["black-friday"],
        "priceInfo": {
            "currencyCode": "USD",
            "price": price,
            "originalPrice": fake.random_int(min=200, max=300),
            "cost": cost
        },
        "availableQuantity": fake.random_int(min=1, max=100),
        "uri": fake.url(),
        "images": [{"uri": fake.image_url(), "height": 320, "width": 320}]
    }

# Generate and write the product catalog
product_catalog = [generate_fake_product(uuid.uuid4(), index) for index in range(1000)]
with open('productPurchased.json', 'w') as f:
    for product in product_catalog:
        f.write(json.dumps(product) + '\n')

# Generate a purchase transaction and product details
def generate_purchase_event_with_details(products):
    selected_product = random.choice(products)
    quantity = fake.random_int(min=1, max=5)
    revenue = selected_product["priceInfo"]["price"] * quantity
    tax = revenue * 0.07  # Assuming a 7% tax rate
    cost = selected_product["priceInfo"]["cost"] * quantity

    # Move the random datetime generation inside this function
    event_datetime = generate_random_datetime(start_date, end_date).isoformat() + "Z"

    purchase_transaction = {
        "id": uuid.uuid4().hex,
        "revenue": revenue,
        "tax": tax,
        "cost": cost,
        "currencyCode": "USD"
    }
    product_details = {
        "product": {
            "id": selected_product["id"],
            "title": selected_product["title"],
            "description": selected_product["description"],
            "categories": selected_product["categories"],
            "attributes": selected_product["attributes"],
            "language_code": selected_product["language_code"],
            "tags": selected_product["tags"],
            "priceInfo": selected_product["priceInfo"],
            "availableQuantity": selected_product["availableQuantity"],
            "uri": selected_product["uri"],
            "images": selected_product["images"]
        },
        "quantity": quantity
    }
    return {
        "eventType": "purchase-complete",
        "visitorId": uuid.uuid4().hex,
        "sessionId": uuid.uuid4().hex,
        "eventTime": event_datetime,  # Use the newly generated event datetime
        "experimentIds": [fake.word() for _ in range(random.randint(1, 3))],
        "attributionToken": fake.sha256(),
        "attributes": {
            fake.word(): {
                "text": [fake.word(), fake.word()],
                "searchable": fake.boolean(),
                "indexable": fake.boolean()
            }
        },
        "productDetails": [product_details],
        "purchaseTransaction": purchase_transaction
    }

# Generate and write purchase events with product details and transaction details
purchase_events = [generate_purchase_event_with_details(product_catalog) for _ in range(1000)]
with open('userEvents-purchase.json', 'w') as f:
    for event in purchase_events:
        f.write(json.dumps(event) + '\n')
