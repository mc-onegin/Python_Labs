import json

with open("ex_2.json") as file:
    data = json.load(file)

with open("ex_2_corrected.json", 'w') as file:
    json.dump(data, file, indent=4)

for user in data:
    print(f"{user['name']}: {user['phoneNumber']}")