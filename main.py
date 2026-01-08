from src.ai.intent_router import detect_intent
from src.ai.response_engine import generate_response
from src.ai.conversation_state import ConversationState
from src.ai.followup_engine import generate_followup

from src.voice.wake_word import listen_for_wake_word
from src.voice.stt import recognize_speech
from src.voice.tts import speak

import time


def main():
    print("LEVEL-2-A: Brain v1 (Intent Routing) active")

    # 🧠 Initialize conversation state ONCE
    state = ConversationState()

    while True:
        # 1️⃣ Wake word
        listen_for_wake_word()

        # 2️⃣ Language selection
        print("Choose language: 1-English | 2-Hindi")
        choice = input("Enter choice: ").strip()
        lang = "hi" if choice == "2" else "en"

        speak("Speak now", lang)
        time.sleep(0.5)

        # 3️⃣ Speech to Text
        text = recognize_speech(language=lang)
        print("You said:", text)

        # 4️⃣ 🧠 Intent Detection
        intent = detect_intent(text, lang)
        print(f"Detected intent: {intent}")

        # 🛑 Stop intent
        if intent == "stop":
            speak("Okay, stopping. Goodbye!", lang)
            break

        # 5️⃣ 🤖 Response Engine
        responses = generate_response(intent, text, lang)

        for msg in responses:
            speak(msg, lang)

        # 6️⃣ 🧠 Update conversation state
        topic = "ai" if "ai" in text.lower() else None
        state.update(intent=intent, topic=topic)

        # 7️⃣ 🔁 Generate follow-up question
        followup = generate_followup(intent, state.current_topic, lang)
        if followup:
            speak(followup, lang)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
