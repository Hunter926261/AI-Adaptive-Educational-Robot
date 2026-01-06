from src.ai.intents.intent_definitions import INTENTS
from src.ai.semantic_matcher import normalize_text

KNOWN_TOPICS = ["ai"]


def detect_intent(text, language="en"):
    normalized_text = normalize_text(text)

    # 🔴 Priority 1: Learning intent
    for keyword in INTENTS["learn_topic"].get(language, []):
        if normalize_text(keyword) in normalized_text:
            return "learn_topic"

    # 🔵 Priority 2: Definition intent (topic-aware)
    for keyword in INTENTS["ask_definition"].get(language, []):
        if normalize_text(keyword) in normalized_text:
            for topic in KNOWN_TOPICS:
                if topic in normalized_text:
                    return "ask_definition"

    # 🟢 Other intents
    for intent, patterns in INTENTS.items():
        if intent in ["learn_topic", "ask_definition"]:
            continue
        for keyword in patterns.get(language, []):
            if normalize_text(keyword) in normalized_text:
                return intent

    return "unknown"
