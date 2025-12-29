from src.voice.wake_word import listen_for_wake_word
from src.voice.stt import recognize_speech

def main():
    print("LEVEL-1-C: Wake word 'hello Guru' active")

    while True:
        listen_for_wake_word()

        print("🗣 Choose language:")
        print("1️⃣ English")
        print("2️⃣ Hindi")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "2":
            language = "hi"
            print("🎧 Hindi STT activated")
        else:
            language = "en"
            print("🎧 English STT activated")

        text = recognize_speech(language=language)
        print("You said:", text)


if __name__ == "__main__":
    main()
