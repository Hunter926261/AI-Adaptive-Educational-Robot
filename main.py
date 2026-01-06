from src.ai.intent_router import detect_intent
from src.ai.response_engine import generate_response
from src.voice.wake_word import listen_for_wake_word
from src.voice.stt import recognize_speech
from src.voice.tts import speak
import time


def main():
    print("LEVEL-2-A: Brain v1 (Intent Routing) active")

    while True:
        # 1. Wake word
        listen_for_wake_word()

        # 2. Language selection
        print("Choose language: 1-English | 2-Hindi")
        choice = input("Enter choice: ").strip()
        lang = "hi" if choice == "2" else "en"

        speak("Speak now", lang)
        time.sleep(0.5)

        # 3. Speech to Text
        text = recognize_speech(language=lang)
        print("You said:", text)

        # 4. 🧠 Intent Detection
        intent = detect_intent(text, lang)
        print(f"Detected intent: {intent}")

        # 🛑 Stop intent (kept as-is)
        if intent == "stop":
            speak("Okay, stopping. Goodbye!", lang)
            break

        # 🤖 Response Engine Integration
        response, example = generate_response(intent, text, lang)
        speak(response, lang)

        if example:
            speak(example, lang)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
