from online.internet import is_internet_available

def should_go_online(intent):
    if intent in ["question"]:
        return True
    return False

def can_use_online(intent):
    return should_go_online(intent) and is_internet_available()
