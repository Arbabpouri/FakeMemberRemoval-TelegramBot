from telethon.types import PeerChannel
from telethon.events import NewMessage
from telethon.custom import Message
from config import Config, bot
from telethon import TelegramClient


class Config:
    
    SESSION_NAME = "MemberCheckerBot"
    API_ID = 123
    API_HASH = ""
    BOT_TOKEN = ""
    CHANNEL_ID = 123
    ADMINS = []


bot = TelegramClient(
    session=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
).start(
    bot_token=Config.BOT_TOKEN
)


@bot.on(NewMessage(incoming=True, chats=Config.ADMINS, func=lambda e: e.message.message.startwith('/check ')))
async def check_channel(event: Message) -> None:
    pass



if __name__ == "__main__":
    print("Bot is online")
    bot.run_until_disconnected()
    