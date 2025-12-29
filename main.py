from src.voice.wake_word import listen_for_wake_word
from src.voice.stt import recognize_speech
from src.voice.tts import speak
import time

def main():
    print("LEVEL-1-D: Full Voice I/O active")

    while True:
        # 1. Wait for wake word
        listen_for_wake_word()

        # 2. Language selection
        print("Choose language: 1-English | 2-Hindi")
        choice = input("Enter choice: ").strip()

        if choice == "2":
            lang = "hi"
            speak("आप क्या कहना चाहते हैं?", "hi")
        else:
            lang = "en"
            speak("What would you like to say?", "en")

        # Small pause to allow TTS to finish cleanly
        time.sleep(0.5)

        # 3. Speech to Text
        text = recognize_speech(language=lang)
        print("You said:", text)

        # 4. MUST speak response (this was missing/skipped earlier)
        print("🔊 Speaking response...")
        if lang == "hi":
            speak(f"आपने कहा: {text}", "hi")
        else:
            speak(f"You said: {text}", "en")


        # Pause before looping back to wake word
        time.sleep(0.5)


if __name__ == "__main__":
    main()
