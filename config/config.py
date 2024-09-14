from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKENS = [token.strip() for token in getenv('BOT_TOKENS', '').split(',') if token.strip()]

