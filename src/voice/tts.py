import pyttsx3

def speak(text, language="en"):
    # Re-initialize engine EVERY time (Windows fix)
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    voices = engine.getProperty("voices")
    selected_voice = voices[0].id  # default English

    if language == "hi":
        for voice in voices:
            if "hi" in voice.id.lower() or "hindi" in voice.name.lower():
                selected_voice = voice.id
                break
        else:
            print("⚠ Hindi voice not available. Using English voice.")

    engine.setProperty("voice", selected_voice)
    engine.say(text)
    engine.runAndWait()
