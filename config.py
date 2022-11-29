from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9683694"))
API_HASH = getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
BOT_TOKEN = getenv("BOT_TOKEN","5583584098:AAFhAbKE9sHvDCp4zfVuh7uVFFh1iCtt1GQ")
BOT_NAME = getenv("BOT_NAME","Tom")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SESSION_NAME = getenv("SESSION_NAME", "AQDDQMI2bFqY_D9SHZkw6bk4_8aMs8OIcbeKBEAf0Gr33Bp0I9cXZfIC7GLLEYER745_OMLA0Kz1pTFRbLcIndXwGvq_Ys4YFLGCWCwhI5kWDuBvP60N4KcB7Dzs8JM_io4LPnkkbE8L1SgaGD4BTseWaxgNdMfbAPo1BCG8tZpyKrXwSPMUTQ5V3soaLSWeZSKIf_zfZNww2mIAqkHrcFUh0GGPY6TY8WByZRa7yTlMykHemMLqSpsx3NHlkmPFAOQXhIlIwp_wtpJauAz4U9nn6i4yFZVZF_9WgBM1ZHQBC5JLMCODdl2lKVkCOW7n9-utjLX4bItwJCdbgamfLMqXAAAAAWSTplYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5448620713").split()))
