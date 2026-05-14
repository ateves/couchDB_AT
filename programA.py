import requests
import json

# Configuration
URL = "http://127.0.0"
DB_NAME = "my_database"

# 1. Create a Database
requests.put(f"{URL}/{DB_NAME}")

# 2. Add a Document
doc = {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "status": "active"
}

response = requests.post(
    f"{URL}/{DB_NAME}", 
    data=json.dumps(doc), 
    headers={"Content-Type": "application/json"}
)

print(response.json())
