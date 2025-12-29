from src.ai.intents.intent_definitions import INTENTS


def detect_intent(text, language="en"):
    text = text.lower()

    for intent, patterns in INTENTS.items():
        keywords = patterns.get(language, [])
        for keyword in keywords:
            if keyword in text:
                return intent

    return "unknown"
