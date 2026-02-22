from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump
from training_data import EMOTION_DATA, INTENT_DATA


def train_emotion_model():
    texts, labels = zip(*EMOTION_DATA)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    dump((vectorizer, model), "emotion_model.joblib")


def train_intent_model():
    texts, labels = zip(*INTENT_DATA)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    dump((vectorizer, model), "intent_model.joblib")


if __name__ == "__main__":
    train_emotion_model()
    train_intent_model()
    print("ML models trained successfully")
