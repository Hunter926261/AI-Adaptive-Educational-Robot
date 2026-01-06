from src.ai.intents.intent_definitions import INTENTS
from src.ai.semantic_matcher import normalize_text


def detect_intent(text, language="en"):
    text = normalize_text(text)

    for intent, patterns in INTENTS.items():
        for keyword in patterns.get(language, []):
            if keyword in text:
                return intent

    return "unknown"
