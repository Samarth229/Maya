from core.emotion import detect_emotion, detect_intent
from core.responder import generate_response
from core.voice import speak
from core.emotion_memory import EmotionMemory

from online.decision_engine import should_go_online
from online.internet import is_internet_available
from online.online_brain import query_online_llm


def start_session(mode="text"):
    if mode == "voice":
        speak("Say maya first, then tell me what you need.")
        print("\nYou can talk to me now.")
        print("Say 'maya' first, then speak your message. Say 'exit' to leave.")
    else:
        print("\nYou can talk to me now.")
        print("You can type your message. Type 'exit' to leave.")

    emotion_memory = EmotionMemory()
    messages = []

    while True:
        if mode == "voice":
            from core.stt import listen_once

            heard = listen_once().lower().strip()
            print(f"> {heard}")

            if not heard:
                continue

            if "exit" in heard:
                speak("Alright, talk to you soon.")
                break

            if "maya" not in heard:
                speak("If you want to talk to me, say maya first.")
                continue

            speak("Yes, I am listening.")
            user_input = listen_once().strip()
            print(f"> {user_input}")

        else:
            user_input = input("> ").strip()

            if user_input.lower() == "exit":
                print("\nAlright, talk to you soon 😊")
                break

        if not user_input or len(user_input) < 2:
            continue

        messages.append(user_input)

        # Detect emotion and intent
        emotion = detect_emotion(user_input)
        intent = detect_intent(user_input)

        # Update emotional memory (handles decay internally)
        emotion_memory.update(emotion)
        sad_level = emotion_memory.current_sad_level()

        # -------------------------
        # SADNESS LOGIC (with decay)
        # -------------------------
        if sad_level > 0:

            if intent == "statement":
                response = generate_response("emotional_support", emotion)

            elif intent == "question":
                if should_go_online(intent) and is_internet_available():
                    answer = query_online_llm(user_input)
                else:
                    answer = generate_response(intent, emotion)

                if emotion_memory.should_add_prefix():
                    prefix = emotion_memory.get_prefix()
                    response = f"{prefix}\n{answer}"
                else:
                    response = answer

            else:
                response = generate_response(intent, emotion)

        # -------------------------
        # HAPPY LOGIC
        # -------------------------
        elif emotion == "happy":

            if intent == "question":
                if should_go_online(intent) and is_internet_available():
                    response = query_online_llm(user_input)
                else:
                    response = generate_response(intent, emotion)
            else:
                response = generate_response("positive_ack", emotion)

        # -------------------------
        # NEUTRAL LOGIC
        # -------------------------
        else:
            if should_go_online(intent) and is_internet_available():
                response = query_online_llm(user_input)
            else:
                response = generate_response(intent, emotion)

        print(response)

        if mode == "voice":
            speak(response, emotion)

    return messages, emotion_memory.emotional_trend()


def extract_important_message(messages):
    if not messages:
        return None

    if isinstance(messages, str):
        messages = [messages]

    low_value_keywords = {
        "hi", "hello", "hey",
        "how are you", "how r u",
        "good morning", "good evening"
    }

    scored_messages = []

    for msg in messages:
        msg_lower = msg.lower()

        if any(k in msg_lower for k in low_value_keywords):
            score = 0
        else:
            score = len(msg.split())

            if any(word in msg_lower for word in ["my", "first", "project", "ai", "bot", "feel"]):
                score += 5

        scored_messages.append((score, msg))

    scored_messages.sort(reverse=True)
    return scored_messages[0][1]




