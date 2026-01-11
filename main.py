from src.ai.intent_router import detect_intent
from src.ai.response_engine import generate_response
from src.ai.conversation_state import ConversationState
from src.ai.followup_engine import generate_followup

# 📘 LEVEL-3 imports
from src.education.lesson_engine import LessonEngine
from src.education.answer_evaluator import evaluate_answer

# 🧠 LEVEL-4-A Learning Tracker
from src.ai.learning_tracker import LearningTracker

# 🎙 Voice modules
from src.voice.wake_word import listen_for_wake_word
from src.voice.stt import recognize_speech
from src.voice.tts import speak

import time


def main():
    print("LEVEL-4-A: Learning Tracker")

    # 🧠 Initialize conversation state ONCE
    state = ConversationState()

    # 📘 Initialize lesson engine ONCE
    lesson_engine = LessonEngine()

    # 🧠 Initialize learning tracker ONCE (STEP-2)
    learning_tracker = LearningTracker()

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

        if not text:
            speak("I did not catch that. Please try again.", lang)
            continue

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

            # 📘 LEVEL-3-A: Auto-start lesson
            if state.current_topic:
                lesson = lesson_engine.start_lesson(state.current_topic)

                if lesson:
                    # 🧠 Teach
                    speak(lesson["concept"], lang)
                    speak(lesson["explanation"][lang], lang)
                    speak(lesson["example"][lang], lang)

                    # ❓ Ask question
                    speak(lesson["question"][lang], lang)

                    # 🟦 Answer Checking
                    speak("Please answer.", lang)
                    user_answer = recognize_speech(language=lang)

                    if not user_answer:
                        speak("No worries. Let's try again next time.", lang)
                    else:
                        is_correct = evaluate_answer(
                            user_answer,
                            lesson["expected_answers"][lang],
                            lang
                        )

                        # 🧠 STEP-2: RECORD LEARNING DATA (silent)
                        learning_tracker.record_attempt(
                            topic=state.current_topic,
                            correct=is_correct
                        )

                        # 🧪 TEMP DEBUG (remove after verification)
                        print("📊 Learning progress:", learning_tracker.progress)


                        if is_correct:
                            speak("Good job! That is correct.", lang)
                        else:
                            speak("Nice try. Let me explain again.", lang)
                            speak(lesson["example"][lang], lang)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
