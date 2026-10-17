import os
import asyncio
from flask import Flask
import threading
from pyrogram import Client, filters
from pyrogram.types import Message

web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot is running 24/7!"

def run_web():
    web_app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_web).start()

API_ID = int(os.getenv("API_ID", "31167565"))
API_HASH = os.getenv("API_HASH", "bec8dcd33707d37c90c6bc4cc1994e5f")
SESSION_STRING = os.getenv("SESSION_STRING")

TARGET_CHANNELS = [
    "RealMadridArabic18",
    "Offsideahdaff",
    "Real_Madrid116",
    "sccor8"
]

COMMENT_TEXT = "The best 🤍"

app = Client("my_session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(filters.chat(TARGET_CHANNELS))
async def auto_comment(client: Client, message: Message):
    try:
        await asyncio.sleep(1)
        await message.reply_text(COMMENT_TEXT)
        print(f"✅ تم التعليق بنجاح في: {message.chat.title}")
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

print("🚀 البوت يعمل الآن على السحاب...")
app.run()
