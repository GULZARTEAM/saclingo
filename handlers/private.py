import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/505bda41f97d408c7dd2c.jpg",
        caption=f"""**ᴛʜɪꜱ ᴍᴜꜱɪᴄ ʙᴏᴛ ɪꜱ ᴀᴅᴠᴀɴᴄᴇ ᴀɴᴅ ɴᴏ ʟᴀɢ ᴜꜱᴇ ɪᴛ ᴄᴏɴᴛɪɴᴜᴏᴜꜱʟʏ .
ᴄᴏᴅᴇʀ :- [ʙᴀᴅᴇ ʟᴏɢ](https://t.me/nobitadev)
ɪꜰ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛᴇʟʟ ʜᴇʀᴇ = [ʙᴀᴅᴇ ʟᴏɢ](https://t.me/nobitadev)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕 ᴄʟᴜꜱᴛᴇʀ 💫", url=f"https://t.me/TJN_MUSIC_BOT?startgroup=true")
                ]
                
           ]
        ),
    )
