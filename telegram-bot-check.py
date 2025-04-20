from telegram import Bot
import os

def check_bot(token: str):
    bot = Bot(token=token)
    print("✅ Bot initialized successfully.")

    info = bot.get_me()
    print(f"🤖 Bot username: {info.username}")
    print(f"🆔 Bot ID: {info.id}")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ BOT_TOKEN not found in environment variables.")
    else:
        check_bot(token)

