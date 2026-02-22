from pathlib import Path

OPENAI_API_KEY = ""

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
USERS_DIR = DATA_DIR / "users"

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
