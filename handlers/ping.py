import time
from datetime import date, datetime
import requests 
from main import bot
from pyrogram import filters
from pyrogram.types import Message


@bot.on_message(filters.command("ping") & filters.all)
async def ping(_, msg: Message):
    start_time = datetime.now()
    end_time = datetime.now()
    uptime = ((end_time - start_time).microseconds / 1000)
    await asst.send_message(msg.chat.id, f"❖𝗣 𝗢 𝗡 𝗚❖ ♪\nᴍs: {uptime}s!!")
