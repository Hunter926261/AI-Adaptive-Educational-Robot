from src.ai.intent_router import detect_intent

tests = [
    ("hello", "en"),
    ("what is artificial intelligence", "en"),
    ("मुझे AI सिखाओ", "hi"),
    ("तुम कौन हो", "hi"),
    ("asdf qwerty", "en")
]

for text, lang in tests:
    intent = detect_intent(text, lang)
    print(f"Input: {text} | Intent: {intent}")
