from telethon.types import PeerChannel
from telethon.events import NewMessage
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.custom import Message
from config import Config, bot
from algoritms import Algoritms


@bot.on(NewMessage(incoming=True, chats=Config.ADMINS, func=lambda e: e.message.message.startwith('/check ')))
async def check_channel(event: Message) -> None:
    channel_id = event.message.message.replace("/check ", "")
    
    if not channel_id.isnumberic():
        return
    
    
    
    



if __name__ == "__main__":
    print("Bot is online")
    bot.run_until_disconnected()
    