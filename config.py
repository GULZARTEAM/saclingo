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
SESSION_NAME = getenv("SESSION_NAME", "AQBtKTtEb0EIJTB0H6hSHJ-2Emh-IFQtuoGhPxrdF9PeTPc2sCHYHCe4sEVQqr3soqxLYDR1v0x40gMrusTrFB_A9YkuSGPbLHSS8fodFWVfpiyrcigNH_a5Ov5FMCnEUY602-1DTfkSXmB5_DFhSrNN-4GekROymdpQuwoPv97oKXnkt2u26NGuC8Q9pHqXAEVpgcxsHkG-ZSunYrGM4lqq0Ym2isLAByBgezfY159IaEnYu4ZKfVOCWZEUxzH_CrtHeYu_23b4O6GPFDPIZcc2NDe2geLCmuU7DMGMTKIc9LmmrsSCMkcj4cGSNaf633NiQJN9zj7upsR0u0SQylxLAAAAAWSTplYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5448620713 1211015395").split()))
