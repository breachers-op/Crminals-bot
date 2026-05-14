"""
Main entry point for Criminals Bot - Telegram Userbot
"""

import os
import asyncio
import logging
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

# --------------------------------------------------
# LOGGING CONFIGURATION
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("criminals-bot")

# --------------------------------------------------
# TELEGRAM API CONFIG
# --------------------------------------------------

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SESSION_STRING = os.getenv("SESSION_STRING")

if not API_ID or not API_HASH:
    raise ValueError(
        "Missing API_ID or API_HASH in .env file"
    )

API_ID = int(API_ID)

# --------------------------------------------------
# CREATE TELEGRAM CLIENT
# --------------------------------------------------

if SESSION_STRING:
    client = TelegramClient(
        StringSession(SESSION_STRING),
        API_ID,
        API_HASH
    )
else:
    client = TelegramClient(
        "criminals_session",
        API_ID,
        API_HASH
    )

# --------------------------------------------------
# SAFE IMPORTS
# --------------------------------------------------

try:
    from handlers.music import register_music_handlers
except Exception as e:
    logger.warning(f"Music handlers not loaded: {e}")

    def register_music_handlers(client):
        pass

try:
    from handlers.admin import register_admin_handlers
except Exception as e:
    logger.warning(f"Admin handlers not loaded: {e}")

    def register_admin_handlers(client):
        pass

try:
    from handlers.utility import register_utility_handlers
except Exception as e:
    logger.warning(f"Utility handlers not loaded: {e}")

    def register_utility_handlers(client):
        pass

# --------------------------------------------------
# BASIC COMMANDS
# --------------------------------------------------

@client.on(events.NewMessage(pattern=r'^\.ping$'))
async def ping_command(event):
    await event.reply("🏓 Pong! Criminals Bot is alive.")


@client.on(events.NewMessage(pattern=r'^\.alive$'))
async def alive_command(event):
    me = await client.get_me()

    text = f"""
🤖 Criminals Bot Online

👤 User: {me.first_name}
🆔 ID: {me.id}
📡 Status: Running
"""

    await event.reply(text)


@client.on(events.NewMessage(pattern=r'^\.help$'))
async def help_command(event):
    help_text = """
╔══════════════════════════════╗
║      CRIMINALS BOT HELP      ║
╚══════════════════════════════╝

🎵 MUSIC COMMANDS
.play <song>
.pause
.resume
.skip
.stop
.queue

👮 ADMIN COMMANDS
.ban
.unban
.kick
.mute
.unmute
.pin
.unpin

🛠 UTILITY COMMANDS
.ping
.alive
.help

⚡ Powered by Telethon
"""

    await event.reply(help_text)

# --------------------------------------------------
# STARTUP MESSAGE
# --------------------------------------------------

async def startup_message():
    me = await client.get_me()

    logger.info("=" * 50)
    logger.info("🤖 Criminals Bot Started Successfully")
    logger.info(f"👤 Logged in as: {me.first_name}")
    logger.info(f"🆔 User ID: {me.id}")

    if me.username:
        logger.info(f"📛 Username: @{me.username}")

    logger.info("=" * 50)

# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------

async def main():
    logger.info("Starting Criminals Bot...")

    # Register custom handlers
    register_music_handlers(client)
    register_admin_handlers(client)
    register_utility_handlers(client)

    await client.start(phone=PHONE_NUMBER)

    await startup_message()

    logger.info("📡 Bot is now listening...")

    await client.run_until_disconnected()

# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == '__main__':
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logger.warning("Bot stopped manually")

    except Exception as e:
        logger.exception(f"Fatal Error: {e}")
