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

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?repository=https://github.com/breachers-op/Crminals-bot)

# 🚀 Session Generator

## Generate Telegram Session
[![Run on Replit](https://replit.com/badge/github/YOUR_USERNAME/Crminals-Session-Generator)](https://replit.com/github/YOUR_USERNAME/Crminals-Session-Generator)

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
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
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

## License

MIT License

## Support

For issues and questions, open an issue on GitHub.
