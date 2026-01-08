class ConversationState:
    def __init__(self):
        self.current_topic = None
        self.last_intent = None

    def update(self, intent, topic=None):
        self.last_intent = intent
        if topic:
            self.current_topic = topic
