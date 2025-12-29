import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

SAMPLE_RATE = 16000

MODELS = {
    "en": Model("models/en"),
    "hi": Model("models/hi")
}


def recognize_speech(language="en", duration=5):
    if language not in MODELS:
        raise ValueError(f"Language '{language}' not supported yet")

    q = queue.Queue()

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    recognizer = KaldiRecognizer(MODELS[language], SAMPLE_RATE)

    print(f"🎧 Listening ({language})...")
    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback,
    ):
        for _ in range(int(SAMPLE_RATE / 8000 * duration)):
            data = q.get()
            recognizer.AcceptWaveform(data)

    result = recognizer.FinalResult()
    text = json.loads(result).get("text", "")
    return text



if __name__ == "__main__":
    print("English:", recognize_speech("en"))
    print("Hindi:", recognize_speech("hi"))
