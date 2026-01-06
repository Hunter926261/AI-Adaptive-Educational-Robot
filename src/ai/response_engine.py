from src.ai.knowledge_base import KNOWLEDGE_BASE


def generate_response(intent, text, language="en"):
    text = text.lower()

    if intent == "ask_definition":
        if "ai" in text:
            topic = KNOWLEDGE_BASE["ai"]
            return [
                topic["definition"][language],
                topic["explanation"][language],
                topic["example"][language]
            ]

    if intent == "learn_topic":
        return [
            "Great! Let’s start learning step by step.",
            "Please tell me which topic you want to begin with."
        ]

    return [
        "I am still learning this topic.",
        "Please try asking in a different way."
    ]
