import requests
from pyrogram import idle
from pyrogram import Client as Bot

from callsmusic import call_py
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
call_py()
idle()
