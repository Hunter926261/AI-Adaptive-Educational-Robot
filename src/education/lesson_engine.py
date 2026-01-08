from src.education.curriculum import CURRICULUM


class LessonEngine:
    def __init__(self):
        self.current_lesson_index = 0

    def start_lesson(self, subject, level="beginner"):
        lessons = CURRICULUM.get(subject, {}).get(level, [])
        if not lessons:
            return None

        self.current_lesson_index = 0
        return lessons[self.current_lesson_index]
