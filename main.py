from pyrogram import Client, filters
import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "hello_world_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        "👋 Hello World!\n\n"
        "Welcome to this Pyrogram bot. Send me any message and I'll respond!"
    )

@app.on_message(filters.text & filters.private)
async def hello_world(client, message):
    await message.reply_text(f"Hello World! You said: {message.text}")

if __name__ == "__main__":
    print("🤖 Starting Hello World Bot...")
    app.run()
