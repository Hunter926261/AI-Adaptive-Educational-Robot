from src.ai.intent_router import detect_intent
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

        # 3. STT
        text = recognize_speech(language=lang)
        print("You said:", text)

        # 4. 🧠 Brain v1
        intent = detect_intent(text, lang)
        print(f"Detected intent: {intent}")

        if intent == "greeting":
            speak("Hello! How can I help you?", lang)

        elif intent == "ask_name":
            speak("I am your AI educational robot.", lang)

        elif intent == "ask_definition":
            speak("Please tell me the topic you want to know about.", lang)

        elif intent == "learn_topic":
            speak("Sure. Tell me the topic you want to learn.", lang)

        elif intent == "stop":
            speak("Okay, stopping. Goodbye!", lang)
            break

        else:
            speak("Sorry, I did not understand. Can you rephrase?", lang)

        time.sleep(0.5)

if __name__ == "__main__":
    main()
