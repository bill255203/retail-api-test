import json
from faker import Faker

fake = Faker()

def generate_product():
    return {
        "id": str(fake.unique.random_int(min=1000, max=9999)),
        "categories": [f"{fake.word()} & {fake.word()} > {fake.word()}"],
        "title": f"{fake.word().capitalize()} {fake.random_element(elements=('sneakers', 't-shirt', 'jacket', 'shorts', 'jeans'))}"
    }

products = {
  "products": [generate_product() for _ in range(100)]
}
with open('fake-data.json', 'w') as f:
    json.dump(products, f, indent=2)
