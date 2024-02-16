from faker import Faker
import json

fake = Faker()

def generate_prediction_request_body(num_events):
    # Generate a list of fake user events
    user_events = [{
        "eventType": "detail-page-view",
        "visitorId": fake.uuid4(),
        "eventTime": fake.iso8601(),
        "userInfo": {
            "userId": fake.uuid4(),
            "ipAddress": fake.ipv4(),
            "userAgent": fake.user_agent()
        },
        "productEventDetail": {
            "productId": fake.ean(length=13)
        }
    } for _ in range(num_events)]

    # Construct the request body with multiple user events
    request_body = {
        "userEvents": user_events,
        "pageSize": 10,
        "filter": "filterOutOfStockItems",
        "params": {
            "returnProduct": True,
            "returnScore": True,
            "strictFiltering": True
        },
        "labels": {
            "label1": "testLabel"
        }
    }

    # Convert the request body to a JSON string
    return json.dumps(request_body, indent=2)

# Specify the number of events you want to generate
num_events = 5
request_body_json = generate_prediction_request_body(num_events)
print(request_body_json)

with open('predict.json', 'w') as f:
    json.dump(request_body_json, f, indent=2)