# Pyrogram Telegram Bot - Hello World

## Overview
A simple Telegram bot built with Pyrogram that responds with "Hello World" messages. This bot demonstrates basic message handling and command processing.

## Recent Changes
- 2025-11-12: Initial project setup with Pyrogram bot structure

## Project Architecture
- `main.py`: Main bot file with message handlers
- Uses Pyrogram library for Telegram Bot API
- Environment-based configuration for API credentials

## Setup Instructions

### 1. Get Telegram API Credentials
- Visit https://my.telegram.org/apps
- Create a new application to get your `API_ID` and `API_HASH`

### 2. Create a Bot
- Talk to [@BotFather](https://t.me/BotFather) on Telegram
- Use `/newbot` command to create a new bot
- Save the bot token you receive

### 3. Configure Environment Variables
You need to set three environment variables:
- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API Hash
- `BOT_TOKEN`: Your bot token from BotFather

### 4. Run the Bot
The bot will automatically start when you run the Repl.

## Features
- `/start` command: Sends a welcome message
- Echo messages: Responds to any text message with "Hello World"
- Private chat only (doesn't respond in groups)
