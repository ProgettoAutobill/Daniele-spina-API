import requests
import yaml

url = "http://localhost:8000/openapi.json"

response = requests.get(url)
schema = response.json()

with open("swaggerAPTSmart.yaml", "w", encoding="utf-8") as f:
    yaml.dump(schema, f, allow_unicode=True)

print("Swagger file generato con successo!")