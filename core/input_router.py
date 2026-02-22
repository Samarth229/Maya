import threading
import queue
from core.stt import listen_once
from core.voice import speak


def choose_interaction_mode():
    speak("How would you like to interact? You can say voice or text.")
    print("\nHow would you like to interact?")
    print("You can SAY or TYPE: voice / text")

    result_queue = queue.Queue()

    def listen_voice():
        try:
            heard = listen_once().lower().strip()
            if heard in ["voice", "text"]:
                result_queue.put(heard)
        except:
            pass

    def listen_text():
        typed = input("> ").lower().strip()
        if typed in ["voice", "text"]:
            result_queue.put(typed)

    voice_thread = threading.Thread(target=listen_voice, daemon=True)
    text_thread = threading.Thread(target=listen_text, daemon=True)

    voice_thread.start()
    text_thread.start()

    mode = result_queue.get()  # waits for FIRST valid input

    return mode


