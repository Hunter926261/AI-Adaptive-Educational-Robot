import os
import pvporcupine
import pyaudio
import struct

ACCESS_KEY = os.getenv("PICOVOICE_ACCESS_KEY")
WAKE_WORD_PATH = "wakewords/hello_guru.ppn"


def listen_for_wake_word():
    if ACCESS_KEY is None:
        raise RuntimeError("PICOVOICE_ACCESS_KEY not set")

    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[WAKE_WORD_PATH]
    )

    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("👂 Listening for wake word: 'hello Guru'")

    try:
        while True:
            pcm = stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )
            pcm = struct.unpack_from(
                "h" * porcupine.frame_length,
                pcm
            )

            result = porcupine.process(pcm)
            if result >= 0:
                print("🟢 Wake word 'hello Guru' detected!")
                return True

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()


if __name__ == "__main__":
    listen_for_wake_word()
