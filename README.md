# Pyrogram Hello World Bot

A simple Telegram bot built with Pyrogram that responds with "Hello World".

## Setup

### 1. Get Telegram API Credentials

1. Go to https://my.telegram.org/auth
2. Log in with your phone number
3. Click on "API development tools"
4. Create a new application to get your `API_ID` and `API_HASH`

### 2. Create a Bot Token

1. Open Telegram and search for @BotFather
2. Send `/newbot` command
3. Follow the prompts to create your bot
4. Copy the bot token provided

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

```bash
export API_ID="your_api_id"
export API_HASH="your_api_hash"
export BOT_TOKEN="your_bot_token"
```

### 5. Run the Bot

```bash
python bot.py
```

## Commands

- `/start` - Start the bot and get a welcome message
- `/hello` - Get a "Hello World!" response
- Any text message - Bot will echo back with "Hello World!" prefix
