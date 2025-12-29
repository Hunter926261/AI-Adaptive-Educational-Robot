import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000
DURATION = 5  # seconds


def record_audio():
    print("🎤 Recording... Speak now")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype=np.int16
    )
    sd.wait()
    print("✅ Recording finished")
    return audio


if __name__ == "__main__":
    audio_data = record_audio()
    print("Audio shape:", audio_data.shape)
