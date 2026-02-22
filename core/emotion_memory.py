import random


class EmotionMemory:
    def __init__(self):
        self.sad_level = 0
        self.history = []

    def update(self, emotion):
        # If user expresses sadness, reset intensity
        if emotion == "sad":
            self.sad_level = 3

        # If user expresses happiness, clear sadness
        elif emotion == "happy":
            self.sad_level = 0

        # Neutral message → decay sadness
        else:
            if self.sad_level > 0:
                self.sad_level -= 1

        self.history.append(emotion)

    def current_sad_level(self):
        return self.sad_level

    def emotional_trend(self):
        return self.history[-5:] if self.history else []

    def should_add_prefix(self):
        # Probability curve based on sadness intensity
        probabilities = {
            3: 0.7,
            2: 0.5,
            1: 0.25,
            0: 0.0
        }

        probability = probabilities.get(self.sad_level, 0)
        return random.random() < probability

    def get_prefix(self):
        if self.sad_level == 3:
            options = [
                "I know things feel heavy right now, but I’ve got you.",
                "I’m still here with you, okay?",
                "We’ll get through this together."
            ]
        elif self.sad_level == 2:
            options = [
                "I’m still here for you.",
                "You’re not alone in this.",
                "Let’s take this step by step."
            ]
        elif self.sad_level == 1:
            options = [
                "I hope things are easing a little.",
                "I’m here if you need me.",
                "We’re doing okay."
            ]
        else:
            return ""

        return random.choice(options)

