from core.voice import speak
from core.stt import listen_once

def get_user_id(mode="text"):
    while True:
        if mode == "voice":
            speak("Who am I speaking with?")
            print("Who am I speaking with?")
            name = listen_once()
            print(f"> {name}")

            speak(f"Did you say {name}? Please say yes or no.")
            confirmation = listen_once().lower()
            print(f"> {confirmation}")

            if "yes" in confirmation:
                return name.strip().lower()

            speak("Okay, let's try again.")

        else:
            name = input("Who am I speaking with? ").strip().lower()
            if name:
                return name


