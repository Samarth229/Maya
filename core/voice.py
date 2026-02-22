import pyttsx3


def speak(text, emotion="neutral"):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    female_voice = None
    for voice in voices:
        if "zira" in voice.name.lower() or "female" in voice.name.lower():
            female_voice = voice.id
            break

    if female_voice:
        engine.setProperty("voice", female_voice)

    if emotion == "sad":
        engine.setProperty("rate", 130)
        engine.setProperty("volume", 0.6)

    elif emotion == "happy":
        engine.setProperty("rate", 190)
        engine.setProperty("volume", 1.0)

    else:
        engine.setProperty("rate", 160)
        engine.setProperty("volume", 0.8)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


