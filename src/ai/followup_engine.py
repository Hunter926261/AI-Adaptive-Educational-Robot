def generate_followup(intent, topic, language="en"):
    if intent == "ask_definition" and topic == "ai":
        if language == "hi":
            return "क्या आप एआई पर एक छोटा सा प्रश्न चाहेंगे?"
        return "Would you like a small quiz on AI?"

    if intent == "learn_topic":
        if language == "hi":
            return "बहुत बढ़िया! क्या हम शुरुआत करें?"
        return "Great! Shall we begin?"

    return None
