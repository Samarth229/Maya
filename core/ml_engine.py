from joblib import load


emotion_vectorizer, emotion_model = load("emotion_model.joblib")
intent_vectorizer, intent_model = load("intent_model.joblib")


def predict_emotion(text):
    X = emotion_vectorizer.transform([text])
    return emotion_model.predict(X)[0]


def predict_intent(text):
    X = intent_vectorizer.transform([text])
    return intent_model.predict(X)[0]
