import json

with open("ex_3.json") as file:
    data = json.load(file)
new_data = {
        "id": 3,
        "total": 100.00,
        "items": [
            {
                "name": "item 4",
                "quantity": 2,
                "price": 50.00
            }
        ]
    }
data['invoices'].append(new_data)
with open("ex_3_corrected.json", 'w') as file:
    json.dump(data, file, indent=4)