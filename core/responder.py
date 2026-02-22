def generate_response(intent, emotion):

    if intent == "emotional_support":
        return (
            "I’m really sorry you’re feeling this way. "
            "You don’t have to go through it alone. I’m here with you."
        )

    if intent == "positive_ack":
        return (
            "That’s really nice to hear. "
            "I’m glad you’re feeling good."
        )

    if intent == "question":
        return "That’s an interesting question. Let me think."

    if intent == "greeting":
        return "Hello! I’m here. How are you feeling today?"

    return "I understand. Please continue."

