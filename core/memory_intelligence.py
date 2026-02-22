def generate_intelligent_summary(important_message, emotional_trend):
    if not important_message:
        return None

    if emotional_trend == "sad":
        return f"User talked about {important_message} and seemed emotionally low."

    if emotional_trend == "happy":
        return f"User talked about {important_message} and sounded positive."

    if emotional_trend == "mixed":
        return f"User discussed {important_message} with mixed emotions."

    return f"User talked about {important_message}."
