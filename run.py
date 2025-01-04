import requests
import json

# Shopify store details
SHOP_NAME = "flowyline-official"  # Replace with your store name
ACCESS_TOKEN = "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"  # Replace with your Admin API access token
API_VERSION = "2025-01"  # Replace with the API version you're using

BASE_URL = f"https://{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}"
print(BASE_URL)

def create_customer(first_name, last_name, email, phone=None, verified_email=False):
    url = f"{BASE_URL}/customers.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }
    customer_data = {
        "customer": {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "verified_email": verified_email,
            "addresses": []
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(customer_data))

    if response.status_code == 201:
        print("Customer created successfully!")
        return response.json()
    else:
        print(f"Failed to create customer: {response.status_code}")
        print(response.json())
        return None

# Example usage
new_customer = create_customer(
    first_name="test John",
    last_name="Doe",
    email="john.doe2@example.com",
    phone="+84389086733",
    verified_email=True
)

print(new_customer)
