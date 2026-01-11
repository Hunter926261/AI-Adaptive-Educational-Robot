class LearningTracker:
    def __init__(self):
        self.progress = {}

    def record_attempt(self, topic, correct):
        if topic not in self.progress:
            self.progress[topic] = {
                "correct": 0,
                "incorrect": 0
            }

        if correct:
            self.progress[topic]["correct"] += 1
        else:
            self.progress[topic]["incorrect"] += 1

    def get_stats(self, topic):
        return self.progress.get(topic, None)
