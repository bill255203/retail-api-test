from faker import Faker
import json
import random

fake = Faker()

def generate_fake_product(product_id):
    return {
        "name": f"projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/{product_id}",
        "id": str(product_id),
        "categories": ["Apparel & Accessories > Shoes"],
        "title": f"{fake.word().capitalize()} sneakers",
        "description": "Sneakers for the rest of us",
        "attributes": {
            "vendor": {
                "text": [f"vendor{fake.random_int(min=100, max=999)}", f"vendor{fake.random_int(min=100, max=999)}"]
            }
        },
        "language_code": "en",
        "tags": ["black-friday"],
        "priceInfo": {
            "currencyCode": "USD",
            "price": fake.random_int(min=50, max=150),
            "originalPrice": fake.random_int(min=200, max=300),
            "cost": fake.random_int(min=20, max=49)
        },
        "availableQuantity": str(fake.random_int(min=1, max=100)),
        "uri": fake.url(),
        "images": [
            {"uri": fake.image_url(), "height": 320, "width": 320}
        ]
    }

def generate_fake_products(n):
    # Adjusted to use a generator for memory efficiency with large numbers
    for product_id in range(1, n+1):
        yield generate_fake_product(product_id)

# Open the file in write mode
with open('products.json', 'w') as f:
    # Generate and write each product to the file
    for product in generate_fake_products(10000):
        # Convert the product to a JSON string and write it to the file followed by a newline
        f.write(json.dumps(product) + '\n')
