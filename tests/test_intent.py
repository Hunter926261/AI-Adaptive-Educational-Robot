from src.ai.intent_router import detect_intent

tests = [
    ("What is artificial intelligence?", "en"),
    ("Explain AI", "en"),
    ("AI kya hota hai?", "hi"),
    ("Artificial intelligence ka matlab", "hi"),
    ("Teach me about AI", "en"),
    ("asdf qwerty", "en")
]

for text, lang in tests:
    print(text, "→", detect_intent(text, lang))
