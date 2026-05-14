"""
Main entry point for Criminals Bot - Telegram Userbot
A feature-rich userbot with music and group management capabilities
"""

import os
import asyncio
import logging
from pathlib import Path
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Telegram API credentials
API_ID = int(os.getenv('API_ID', '0'))
API_HASH = os.getenv('API_HASH', '')
PHONE_NUMBER = os.getenv('PHONE_NUMBER', '')
SESSION_STRING = os.getenv('SESSION_STRING', '')

# Validate credentials
if not API_ID or not API_HASH:
    logger.error("API_ID and API_HASH are required. Please set them in .env file")
    exit(1)

# Initialize Telegram client
if SESSION_STRING:
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
else:
    client = TelegramClient('userbot_session', API_ID, API_HASH)

# Import handlers
from handlers.music import register_music_handlers
from handlers.admin import register_admin_handlers
from handlers.utility import register_utility_handlers


async def startup_message():
    """Display startup message"""
    try:
        me = await client.get_me()
        logger.info(f"✅ Bot started successfully as @{me.username}")
        logger.info(f"Name: {me.first_name}")
    except Exception as e:
        logger.error(f"Error getting user info: {e}")


async def main():
    """Main bot function"""
    logger.info("🤖 Starting Criminals Bot...")
    
    # Register all event handlers
    register_music_handlers(client)
    register_admin_handlers(client)
    register_utility_handlers(client)
    
    async with client:
        await startup_message()
        logger.info("📡 Bot is listening for messages...")
        await client.run_until_disconnected()


@client.on(events.NewMessage(pattern=r'^\.help$'))
async def help_command(event):
    """Display help message with all available commands"""
    help_text = """
╔════════════════════════════════════════╗
║   🤖 CRIMINALS BOT - HELP MENU 🤖     ║
╚════════════════════════════════════════╝

📀 MUSIC COMMANDS:
  `.play <query>` - Play music from YouTube
  `.pause` - Pause current playback
  `.resume` - Resume playback
  `.stop` - Stop music
  `.skip` - Skip to next song
  `.queue` - Show current queue
  `.current` - Show currently playing song
  `.volume <0-100>` - Set volume level

👨‍💼 ADMIN COMMANDS:
  `.ban <user>` - Ban user from group
  `.unban <user>` - Unban user
  `.kick <user>` - Kick user from group
  `.mute <user>` - Mute user
  `.unmute <user>` - Unmute user
  `.pin <message>` - Pin message
  `.unpin` - Unpin message
  `.promote <user>` - Promote user to admin
  `.demote <user>` - Demote admin

🛠 UTILITY COMMANDS:
  `.ping` - Check bot status
  `.info` - Get user/chat info
  `.help` - Show this menu

════════════════════════════════════════
Made with ❤️ by breachers-op
    """
    await event.reply(help_text)


if __name__ == '__main__':
    if PHONE_NUMBER and not SESSION_STRING:
        logger.info("First time setup - Please follow the authentication process")
        logger.info(f"Authenticating with {PHONE_NUMBER}...")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
