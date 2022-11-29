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
SESSION_NAME = getenv("SESSION_NAME", "AQAZ2sVNNNn9inIoK1246_7SRQwhAM6UioMdP7dXROarQQW8FBvaljCU4UXKsW4rdgs9KK0l6JkQagyDBS-jcHMNvR8p3iWsExp7ol9pr6HLc7QQDbzemKhvHnz5pWDWnBUoTIZcpmotIANlB0VGDW1bJIUdIYCrdtCvSmiMdjgeZB7T5n-3HKSNNIYnqgMyRPea0wx-SUgN9f6fQCeAxEHQ0adJdkeB_rDjds-gGU7YkcVCeU_IKYmxZaG_53Bh1FhFakga9ijhlZJiutZTQw8txzF2QzF7ZJ4xQH7fEsaN87Kl1YHR-Vr3jrDWPP3fzwNEONAf1RrM5TxQrdEwSQAAAAAWSTplYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5448620713").split()))
