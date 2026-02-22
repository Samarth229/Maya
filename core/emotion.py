from core.ml_engine import predict_emotion, predict_intent


def _rule_based_emotion(text):
    text = text.lower()

    sad_keywords = [
        "sad", "low", "depressed", "upset", "tired",
        "lonely", "hurt", "bad", "not good"
    ]

    happy_keywords = [
        "happy", "excited", "great", "good", "awesome",
        "amazing", "love", "nice"
    ]

    if any(word in text for word in sad_keywords):
        return "sad"

    if any(word in text for word in happy_keywords):
        return "happy"

    return "neutral"


def _rule_based_intent(text):
    text = text.lower().strip()

    question_starters = [
        "what", "why", "how", "when", "where",
        "who", "which", "can", "does", "do", "is"
    ]

    if "?" in text:
        return "question"

    if any(text.startswith(word + " ") for word in question_starters):
        return "question"

    greetings = ["hi", "hello", "hey"]
    if any(text.startswith(g) for g in greetings):
        return "greeting"

    return "statement"


def detect_emotion(text):
    # 🔒 RULES FIRST (trusted)
    rule_emotion = _rule_based_emotion(text)

    # If rules detect strong emotion, trust them
    if rule_emotion in {"sad", "happy"}:
        return rule_emotion

    # 🤖 ML only for neutral cases
    try:
        ml_emotion = predict_emotion(text)
        if ml_emotion in {"sad", "happy", "neutral"}:
            return ml_emotion
    except Exception:
        pass

    return "neutral"


def detect_intent(text):
    try:
        intent = predict_intent(text)
        if intent in {"question", "greeting", "statement"}:
            return intent
    except Exception:
        pass

    return _rule_based_intent(text)


