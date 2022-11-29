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
SESSION_NAME = getenv("SESSION_NAME", "AQBxpCiqbLWPi3QzMLpjV_3eqaTzwaWVvgm-l2LTxKEkI-36V8_hstbkoOltA1Xld_mJInp8q16Zr8K16WzgQwgxULfmEvcJww_54GibMblg2PVBK_3F_PLm2oxS1v1-L-tXRN8jL1VisojQrIJhPRpP2oiFecB7JbD2FqpgtbXzfrNric2MrgJ2jY8ise1QBnrhqAvkVSxYfS-lu7bAtz2D-rs1xdtP51gYPdCKza5SLwEUkOXLTKxI02-1ygOA0x89f8n09C1TZdioz53m0u8HcguH6TzCsEpr-UuSqYfeYhIOq7FEKpKvxYvSgdHoCuilS8bSMgcV5h3hTsiYoKDEAAAAAWSTplYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5448620713").split()))
