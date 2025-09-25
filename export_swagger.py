import requests
import yaml


url = "http://localhost:8000/openapi.json"
schema = requests.get(url).json()


def fix_schema(obj):
    """Ripulisce lo schema da anyOf nullable."""
    if isinstance(obj, dict):
        if "anyOf" in obj:
            types = [o.get("type") for o in obj["anyOf"] if isinstance(o, dict)]
            if "null" in types:
                non_null = [o for o in obj["anyOf"] if o.get("type") != "null"]
                if len(non_null) == 1:
                    obj.update(non_null[0])
                    obj["nullable"] = True
                del obj["anyOf"]
        for k, v in obj.items():
            obj[k] = fix_schema(v)
    elif isinstance(obj, list):
        return [fix_schema(i) for i in obj]
    return obj


# Fix schema
schema = fix_schema(schema)
schema["openapi"] = "3.0.3"

# -------------------------------
# Esempi di request e response
# -------------------------------
examples_data = {
    "/control": {
        "post": {
            "request": {
                "start_scan": {
                    "summary": "Comando start_scan",
                    "description": "Invia al robot il comando start_scan",
                    "value": {"command": "start_scan"}
                },
                "stop": {
                    "summary": "Comando stop",
                    "description": "Ferma il robot",
                    "value": {"command": "stop"}
                }
            },
            "response": {
                "200": {
                    "in_esecuzione": {
                        "summary": "Comando in esecuzione",
                        "value": {"message": "Comando ricevuto: start_scan", "status": "in esecuzione"}
                    }
                }
            }
        }
    }
}


# Funzione per iniettare esempi
def inject_examples(schema, examples):
    for path, methods in examples.items():
        if path not in schema.get("paths", {}):
            continue
        for method, ex in methods.items():
            if method not in schema["paths"][path]:
                continue
            # Request examples
            request_examples = ex.get("request")
            if request_examples:
                content = schema["paths"][path][method].get("requestBody", {}).get("content", {}).get("application/json", {})
                if content is not None:
                    content["examples"] = request_examples
            # Response examples
            response_examples = ex.get("response")
            if response_examples:
                for status_code, examples_dict in response_examples.items():
                    response = schema["paths"][path][method].get("responses", {}).get(status_code, {})
                    if "content" not in response:
                        response["content"] = {}
                    if "application/json" not in response["content"]:
                        response["content"]["application/json"] = {}
                    response["content"]["application/json"]["examples"] = examples_dict
                    schema["paths"][path][method]["responses"][status_code] = response
    return schema

schema = inject_examples(schema, examples_data)

with open("swaggerAPTSmart.yaml", "w", encoding="utf-8") as f:
    yaml.dump(schema, f, allow_unicode=True)

print("Swagger file generato con successo!")
