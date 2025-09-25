from typing import Dict


def api_docs(summary: str, params: Dict[str, str], response: str) -> Dict[str, str]:
    description = summary + "\n\n"
    description += "### Parametri:\n"
    for name, desc in params.items():
        description += f"- **{name}**: {desc}\n"
    description += f"\n### Risposta:\n{response}"
    return {"summary": summary, "description": description}