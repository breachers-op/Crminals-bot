"""
Telegram Session Generator for Criminals Bot
Supports both UserBot and Music Bot session generation
"""

import asyncio
import sys
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


async def generate_session():
    """Generate a Telegram session interactively"""
    
    print("\n" + "="*60)
    print("🔐 Telegram Session Generator - Criminals Bot")
    print("="*60 + "\n")
    
    # Get credentials
    print("⚠️  Get your API credentials from: https://my.telegram.org/apps\n")
    
    api_id = input("📱 Enter your API_ID: ").strip()
    if not api_id.isdigit():
        print("❌ Invalid API_ID. Must be a number.")
        return
    
    api_hash = input("🔑 Enter your API_HASH: ").strip()
    if not api_hash or len(api_hash) < 32:
        print("❌ Invalid API_HASH.")
        return
    
    phone = input("☎️  Enter your phone number (with country code, e.g., +1234567890): ").strip()
    if not phone.startswith('+'):
        print("❌ Phone number must start with '+'")
        return
    
    # Choose session type
    print("\n📋 Choose session type:")
    print("   1. UserBot Session (main bot features)")
    print("   2. Music Bot Session (music player features)")
    session_type = input("\nSelect (1 or 2): ").strip()
    
    if session_type == "1":
        session_name = "criminals_userbot"
        print(f"\n✅ Generating UserBot session: {session_name}")
    elif session_type == "2":
        session_name = "criminals_musicbot"
        print(f"\n✅ Generating Music Bot session: {session_name}")
    else:
        print("❌ Invalid selection. Please choose 1 or 2.")
        return
    
    # Create client and generate session
    client = TelegramClient(session_name, int(api_id), api_hash)
    
    try:
        await client.connect()
        
        # Send code request
        if not await client.is_user_authorized():
            await client.send_code_request(phone)
            
            # Get verification code
            code = input("\n📨 Enter the verification code Telegram sent you: ").strip()
            
            try:
                await client.sign_in(phone, code)
            except SessionPasswordNeededError:
                # Handle 2FA
                password = input("🔐 Two-factor authentication is enabled.\n   Enter your password: ")
                await client.sign_in(password=password)
        
        # Get user info
        me = await client.get_me()
        
        print("\n" + "="*60)
        print("✅ SUCCESS! Session generated successfully!")
        print("="*60)
        print(f"👤 Logged in as: {me.first_name} {me.last_name or ''}")
        print(f"🆔 User ID: {me.id}")
        print(f"📱 Phone: {me.phone}")
        print(f"📁 Session file: {session_name}.session")
        print("="*60 + "\n")
        
        print("📥 Download Instructions:")
        print("   1. Download the .session file from the file explorer")
        print("   2. Add it to your bot deployment")
        print("   3. Update your bot config to use this session\n")
        
        print("⚠️  SECURITY WARNING:")
        print("   • Never share your .session file")
        print("   • It contains sensitive authentication data")
        print("   • Keep it safe and private\n")
        
        await client.disconnect()
        
    except Exception as e:
        print(f"\n❌ Error during session generation: {str(e)}")
        print("\n🔧 Troubleshooting:")
        print("   • Check that API_ID and API_HASH are correct")
        print("   • Ensure phone number format is correct (+country code)")
        print("   • Verify the verification code is correct")
        print("   • If using 2FA, ensure password is correct\n")
        await client.disconnect()


def main():
    """Main entry point"""
    try:
        asyncio.run(generate_session())
    except KeyboardInterrupt:
        print("\n\n⏹️  Session generation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
