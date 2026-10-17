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

@app.on_message(filters.chat(TARGET_CHANNELS))
async def auto_comment(client: Client, message: Message):
    try:
        await asyncio.sleep(1)
        await message.reply_text(COMMENT_TEXT)
        print(f"✅ تم التعليق بنجاح في القناة: {message.chat.title}")
    except Exception as e:
        print(f"❌ خطأ أثناء إرسال التعليق: {e}")

async def main():
    async with app:
        print("🚀 جاري بدء تشغيل البوت وتسجيل القنوات المستهدفة...")
        
        # إجبار البوت على جلب القنوات وتخزينها في ذاكرة الجلسة لمنع خطأ Peer ID
        for channel in TARGET_CHANNELS:
            try:
                chat = await app.get_chat(channel)
                print(f"✅ تم ربط وتخزين القناة بنجاح: {chat.title} (ID: {chat.id})")
            except Exception as e:
                print(f"⚠️ تنبيه بخصوص القناة {channel}: {e}")

        print("🎉 البوت متصل الآن ويراقب القنوات بانتظار المنشورات الجديدة...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    app.run(main())
