from pyrogram import Client, filters
from pyrogram.types import Message
import os

# Get credentials from environment variables
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Create the Pyrogram client
app = Client(
    "helloworld_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """Handle the /start command"""
    await message.reply_text("Hello World! Welcome to the bot.")


@app.on_message(filters.command("hello"))
async def hello_command(client: Client, message: Message):
    """Handle the /hello command"""
    await message.reply_text("Hello World!")


@app.on_message(filters.text & filters.private)
async def echo_message(client: Client, message: Message):
    """Echo back any text message with Hello World prefix"""
    await message.reply_text(f"Hello World! You said: {message.text}")


if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
