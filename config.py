from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN","")
BOT_NAME = getenv("BOT_NAME", "Asisstant") 
API_ID = int(getenv("API_ID",""))
API_HASH = getenv("API_HASH","")
BOT_USERNAME = getenv("BOT_USERNAME", "SOmusiqi_Bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS","1280040987").split()))
