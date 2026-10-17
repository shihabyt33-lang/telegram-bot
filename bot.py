import asyncio
import os

try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID", "31167565"))
API_HASH = os.getenv("API_HASH", "bec8dcd33707d37c90c6bc4cc1994e5f")
SESSION_STRING = os.getenv("SESSION_STRING")

# أسماء القنوات المستهدفة باليوزرنيم بدون @
TARGET_CHANNELS = [
    "RealMadridArabic18",
    "Offsideahdaff",
    "Real_Madrid116",
    "sccor8"
]

COMMENT_TEXT = "The best 🤍"

app = Client(
    "my_bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# استخدام فلتر عام للقنوات وتصفيتها بالاسم لتجنب أي أخطاء في المعرفات
@app.on_message(filters.channel)
async def auto_comment(client: Client, message: Message):
    if message.chat.username and message.chat.username in TARGET_CHANNELS:
        try:
            await asyncio.sleep(2)  # انتظار بسيط وطبيعي
            await message.reply_text(COMMENT_TEXT)
            print(f"✅ تم التعليق بنجاح في القناة: {message.chat.title}")
        except Exception as e:
            print(f"❌ خطأ أثناء إرسال التعليق: {e}")

if __name__ == "__main__":
    print("🚀 البوت يعمل الآن بكامل طاقته ويراقب القنوات...")
    app.run()
