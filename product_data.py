from faker import Faker
import json
import random

fake = Faker()

def generate_fake_product(product_id):
    return {
        "name": f"projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/{product_id}",
        "id": str(product_id),
        "categories": "Apparel & Accessories > Shoes",
        "title": f"{fake.word().capitalize()} sneakers",
        "description": "Sneakers for the rest of us",
        "attributes": {"vendor": {"text": [f"vendor{fake.random_int(min=100, max=999)}", f"vendor{fake.random_int(min=100, max=999)}"]}},
        "language_code": "en",
        "tags": ["black-friday"],
        "priceInfo": {
            "currencyCode": "USD", "price": fake.random_int(min=50, max=150), "originalPrice": fake.random_int(min=200, max=300), "cost": fake.random_int(min=20, max=49)
        },
        # "availableTime": fake.iso8601(tzinfo=None, end_datetime=None),
        "availableQuantity": str(fake.random_int(min=1, max=100)),
        "uri": fake.url(),
        "images": [
            {"uri": fake.image_url(width=None, height=None), "height": 320, "width": 320 }
        ]
    }

def generate_fake_products(n):
    return [generate_fake_product(product_id) for product_id in range(1, n+1)]

# Generate 50 fake products
fake_products = generate_fake_products(50)

# Print the data to the console
for product in fake_products:
    print(json.dumps(product, indent=2))

# Optionally, write the data to a JSON file
with open('prod_data.json', 'w') as f:
    json.dump(fake_products, f, indent=2)
