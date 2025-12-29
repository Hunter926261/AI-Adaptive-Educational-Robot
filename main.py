from src.voice.stt import recognize_speech

def main():
    print("LEVEL-1-B: Offline STT (EN + HI)")

    text = recognize_speech(language="en")
    print("English:", text)

    text = recognize_speech(language="hi")
    print("Hindi:", text)

if __name__ == "__main__":
    main()
