import json
from datetime import datetime
from config import USERS_DIR, DATE_FORMAT


def load_or_create_profile(user_id):
    user_dir = USERS_DIR / user_id
    profile_path = user_dir / "profile.json"

    user_dir.mkdir(parents=True, exist_ok=True)

    if profile_path.exists():
        with open(profile_path, "r", encoding="utf-8") as f:
            profile = json.load(f)
            return profile, False

    now = datetime.now().strftime(DATE_FORMAT)

    profile = {
        "user_name": user_id,
        "first_seen": now,
        "last_seen": now
    }

    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)

    return profile, True


def update_last_seen(user_id):
    profile_path = USERS_DIR / user_id / "profile.json"

    if not profile_path.exists():
        return

    with open(profile_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    profile["last_seen"] = datetime.now().strftime(DATE_FORMAT)

    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)

def load_conversation(user_id):
    conversation_path = USERS_DIR / user_id / "conversation.json"

    if conversation_path.exists():
        with open(conversation_path, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "last_topic": None,
        "summary": None
    }


def save_conversation(user_id, last_topic, summary):
    conversation_path = USERS_DIR / user_id / "conversation.json"

    conversation = {
        "last_topic": last_topic,
        "summary": summary
    }

    with open(conversation_path, "w", encoding="utf-8") as f:
        json.dump(conversation, f, indent=4)


