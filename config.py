from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9683694"))
API_HASH = getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
BOT_TOKEN = getenv("BOT_TOKEN","5443960179:AAF3nIh-qh5rdKMepTEIcM9t1NcIYS9mWys")
BOT_NAME = getenv("BOT_NAME","Tom")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SESSION_NAME = getenv("SESSION_NAME", "AQDD0-3YzrOM5oVzlk6vOD-HBh3m4rPRP-Z-8EESeIAscj08pC2FGLg8FdYnR8InhT0wV-M4JOUyjXSicfTeN5ymeY6WwbXDE3ejepPKgutXYFBtywG35ft6jBLoTfh0rUBkYJvShoOKKiHWJSdO0LcWyLGgXCjGU1gEKKiBCchkhUmBhkQPSRq4ipNJ3R_exYtRTdibCW-2F3gpKLx1cJmKoTDg8WbKoYzAG0cesJJmuGhXfkQ0U60cbSIIBayLvhq_FD_VLDulvFG7qHZFglgaz1LXrvfBAJzgpMBJrDAVd_nUrTEH3RNoTeDTUkKG2SkC_3sH4kTqogp1qxp7TL9oAAAAAUR_1oAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
