from core.input_router import choose_interaction_mode
from core.identity import get_user_id
from core.memory import (
    load_or_create_profile,
    update_last_seen,
    load_conversation,
    save_conversation
)
from core.session import start_session, extract_important_message
from core.memory_intelligence import generate_intelligent_summary


def main():
    print("Starting Maya...")
    from core.voice import speak
    speak("Starting up.")

    from online.online_brain import warm_up_llm
    warm_up_llm()


    mode = choose_interaction_mode()
    
    speak(f"You chose {mode} mode.")
    print(f"You chose {mode} mode.")

    user_id = get_user_id(mode)

    profile, is_new_user = load_or_create_profile(user_id)
    conversation = load_conversation(user_id)

    if is_new_user:
        print(f"\nNice to meet you, {profile['user_name'].title()}.")
    else:
        print(f"\nWelcome back, {profile['user_name'].title()}.")

        if conversation["summary"]:
            print("Last time we talked about:")
            print(conversation["summary"])

    messages, emotional_trend = start_session(mode)

    important_message = extract_important_message(messages)

    if important_message:
        summary = generate_intelligent_summary(
            important_message,
            emotional_trend
        )

        save_conversation(user_id, important_message, summary)

    update_last_seen(user_id)


if __name__ == "__main__":
    main()

