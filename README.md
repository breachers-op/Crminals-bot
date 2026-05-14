# Criminals Bot - Telegram Userbot

A powerful Telegram userbot built with Telethon featuring music management and group/channel management capabilities.

## Features

### 🎵 Music Bot
- Download music from YouTube, Spotify, and SoundCloud
- Queue management
- Play, pause, skip, and stop controls
- Playlist support
- Audio format conversion
- Volume control

### 👥 Group/Channel Management
- Auto-moderation (spam detection, keyword filtering)
- Member management (welcome messages, auto-remove)
- Pin/unpin messages
- Auto-pin important messages
- Member greeting system
- Anti-spam features

## Prerequisites

- Python 3.8+
- Telegram account
- Telegram API credentials from [my.telegram.org/apps](https://my.telegram.org/apps)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/breachers-op/Crminals-bot.git
   cd Crminals-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your credentials:
   - `API_ID` and `API_HASH` from Telegram
   - `PHONE_NUMBER` (your Telegram phone number)
   - Music API keys (YouTube, Spotify)

5. **Run the bot**
   ```bash
   python main.py
   ```

## Getting Telegram API Credentials

1. Go to [https://my.telegram.org/apps](https://my.telegram.org/apps)
2. Login with your Telegram account
3. Fill the form with app details
4. Copy your `API_ID` and `API_HASH`
5. Add them to `.env` file

## 🚀 Session Generator

Generate Telegram sessions for both UserBot and Music Bot directly on Replit:

[![Run on Replit](https://replit.com/badge/github/breachers-op/Crminals-bot)](https://replit.com/github/breachers-op/Crminals-bot)

### How to Generate a Session:

1. Click the "Run on Replit" button above
2. Follow the interactive prompts:
   - Enter your `API_ID` (from [my.telegram.org/apps](https://my.telegram.org/apps))
   - Enter your `API_HASH` (from [my.telegram.org/apps](https://my.telegram.org/apps))
   - Enter your phone number with country code (e.g., +1234567890)
   - Choose session type (1 for UserBot, 2 for Music Bot)
3. Enter the verification code Telegram sends
4. If 2FA is enabled, enter your password
5. Download the generated `.session` file
6. Add it to your bot deployment

**Alternative Method (Local):**
```bash
python session_generator.py
```

## Usage

### Commands

#### Music Commands
- `.play <song>` - Play a song
- `.pause` - Pause current song
- `.resume` - Resume playback
- `.skip` - Skip to next song
- `.stop` - Stop music
- `.queue` - Show queue
- `.nowplaying` - Show current song

#### Group Management Commands
- `.ban <user>` - Ban user
- `.kick <user>` - Kick user
- `.mute <user>` - Mute user
- `.unmute <user>` - Unmute user
- `.purge <count>` - Delete messages
- `.pin` - Pin message
- `.unpin` - Unpin message

## Project Structure

```
Crminals-bot/
├── main.py                 # Entry point
├── config.py              # Configuration
├── session_generator.py   # Session generation tool
├── requirements.txt       # Dependencies
├── requirements-session.txt # Session generator dependencies
├── .env.example          # Environment template
├── .replit               # Replit configuration
├── handlers/             # Command handlers
│   ├── music.py         # Music bot commands
│   ├── management.py    # Group management commands
│   └── admin.py         # Admin commands
├── utils/               # Utility functions
│   ├── music_utils.py   # Music utilities
│   ├── download.py      # Download utilities
│   └── helpers.py       # Helper functions
├── modules/             # Core modules
│   ├── music_player.py  # Music player logic
│   ├── queue.py         # Queue management
│   └── moderator.py     # Moderation logic
└── downloads/           # Downloaded music storage
```

## Warning ⚠️

- This is a userbot for personal use only
- Violating Telegram's Terms of Service may result in account ban
- Use responsibly and ethically
- Do not use for spam or abuse
- **Never share your `.session` files** - they contain sensitive authentication data

## License

MIT License

## Support

For issues and questions, open an issue on GitHub.
