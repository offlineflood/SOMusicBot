from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgBGOwbX2BTpo0giW0MBpuDbwCcLZGvl4b-3acytp_Rvb9PM89c3o2JfyK171aGYsRxSoPCmXvXWoXRAONBMO11GbI5COj-kcdcefXQg4T3sHLuEgIHenXfIFYhj9DzQuqDqlGkzhG_fNq6Rj47pTKwyCRSEe7mvA7uXu8UMhofb0nJoZboqYbMJElHfp1Tpocv6JRFHF5tjD6C_EoPMeuaBMwATX8hk3F6nLAvk_xcPSAxym0pdEQw1rLB6uu580jSeD6QeCAecuj2pH765Dugch_NJ5Ma2WtWhOQqxdHh37YFEe3qfmhRLeKAsfaso0mDZbhqSqaSF38fRzpMLMZKSAAAAAT-zwaUA")
BOT_TOKEN = getenv("BOT_TOKEN","5337183930:AAEQc8pbjleTSxzyjtS_GHYWfeVvcy4pEKo")
BOT_NAME = getenv("BOT_NAME", "Asisstant") 
API_ID = int(getenv("API_ID","16157584"))
API_HASH = getenv("API_HASH","2167d4e6007a79eed91d084bf5b8966a")
BOT_USERNAME = getenv("BOT_USERNAME", "SOmusiqi_Bot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS","1280040987").split()))
