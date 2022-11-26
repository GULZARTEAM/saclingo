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
SESSION_NAME = getenv("SESSION_NAME", "AQACmc1owTlpsmWnJbLk3W1Qk3QGf7cAvY8fEHrVors_4qpJpuxGChbelIPIBVjQnB_834957IWljNQ4A_JTJhlwil8zVVGz8pJUbDVilGQPIekpynrMKmTp3bF9u5rxOFqFpyAKENC-jxFPSBMIZA-3wX_x9AvnbcoQac7HYdji5LU-PqTNkPsyzFwMw_8eNALr9PZNRHT7TQqRndVvy7sKnt-BbbU8sXAnoQRcVp7d3DhKGRIKhnzuMSCrE5jEBQkcuf7629mtjNAuuj9nIsJQq7im0y5pAKbTgsiY6IYWUcAxhHQxzHzBsOjhorLYfjRTHqfnMuRS0KHXjpGI8rmyAAAAAWGlfJIA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
