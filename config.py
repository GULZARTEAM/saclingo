from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9683694"))
API_HASH = getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
BOT_TOKEN = getenv("BOT_TOKEN","5202259558:AAFPK3qOkm_f1lH-UwT_0RIHQNdRWOUE_kY")
BOT_NAME = getenv("BOT_NAME","Tom")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SESSION_NAME = getenv("SESSION_NAME", "AQCXyfDw3aH7qLpLonMdAWsFBrcxmX6ocj8PZ3dTn7qboLK-Cn8rKIAU9hyqk_rwFCAFFwrJZG5gSDN89yVXAlcJcHlGb7F7qd4NKVHA7PVDQBCW8cga-0trDnOKxeMqKww8Jx7ZIr7iqk1eLZ17ATF4bNsttq2bQgkPdW1idj6lpKFoz9nmt80QTcMFIFJeZ7s217dQUmsO3gX9Dfq_q3IViSNqMMK5pVWghnPQ_33mvVOVYczEnBb_qMV9Ea0H7yhB2cejZDe23wkB_VpyNHwhkd7oYj1bzfzOZOAsQzeQ4QE0SeckqXMersrjPDsqMTXlzoeETxOZi6ce0XlDWToxAAAAAWSTplYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5448620713 1211015395").split()))
