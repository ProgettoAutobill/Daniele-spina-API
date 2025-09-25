import requests
import yaml

url = "http://localhost:8000/openapi.json"
schema = requests.get(url).json()

def fix_schema(obj):
    if isinstance(obj, dict):
        # Fix "anyOf" nullable
        if "anyOf" in obj:
            types = [o.get("type") for o in obj["anyOf"] if isinstance(o, dict)]
            if "null" in types:
                non_null = [o for o in obj["anyOf"] if o.get("type") != "null"]
                if len(non_null) == 1:
                    obj.update(non_null[0])   # copy main schema
                    obj["nullable"] = True
                del obj["anyOf"]

        for k, v in obj.items():
            obj[k] = fix_schema(v)

    elif isinstance(obj, list):
        return [fix_schema(i) for i in obj]

    return obj

# fix schema
schema = fix_schema(schema)

# force openapi version
schema["openapi"] = "3.0.3"

# export yaml
with open("swaggerAPTSmart.yaml", "w", encoding="utf-8") as f:
    yaml.dump(schema, f, allow_unicode=True)

print("Swagger file fixato e generato con successo!")