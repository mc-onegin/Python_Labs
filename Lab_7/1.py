import json
import jsonschema

with open("1.error.json") as file:
    data = json.load(file)

with open("json_schema.json") as file:
    schema = json.load(file)


try:
    jsonschema.validate(instance=data, schema=schema)
    print("Validation success")
except jsonschema.exceptions.ValidationError as e:
    print(f"Error: {e.message}")