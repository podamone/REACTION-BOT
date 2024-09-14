from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID", "")

API_HASH = getenv("API_HASH", "")

BOT_TOKENS = [token.strip() for token in getenv('BOT_TOKENS', '').split(',') if token.strip()]

