from src.ai.knowledge_base import KNOWLEDGE_BASE


def generate_response(intent, text, language="en"):
    text = text.lower()

    if intent == "ask_definition":
        if "ai" in text:
            data = KNOWLEDGE_BASE["ai"]
            return (
                data["definition"][language],
                data["example"][language]
            )

    return (
        "I am still learning this topic.",
        "Please try another question."
    )
