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
SESSION_NAME = getenv("SESSION_NAME", "AQAQRIJ2sfOcyrkQ9rqaBjPO68dkVnQpwUcu7muc4PhOBsfGxu2qr0-GpeUi249MVlssFU775ytLcBsqK3o-A7S2g_6v8kdwYla-locRuTlZpdjsuollj2VWL0W2yBnOhUGyiHIpEDWNHImQJmkmpp_gG3vWBiD1ws5w6ig4jqepHGndwkBE_z-S8mbka2jVQR3Xqp55D1KWWNLGKVvFTeYufIu9YDxRzr8QNyrp4MVetd_Lrn9RObTLFtg5v9_nkh1uGUcXTHviuesydukGn-QM9VK1KRZlKJaMG3MjtoBoFcS1YfmixJGG2TgAy4fw1skmuGKuJJAgWc4rTcE6k66aAAAAAU-3erMA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
