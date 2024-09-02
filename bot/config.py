from telethon import TelegramClient


class Config:
    
    SESSION_NAME = "NovinMemberCheckerBot"
    API_ID = 10603708
    API_HASH = "f17d354888d912173f1599ca3133e04e"
    # BOT_TOKEN = "7422604519:AAEmjyucnT1eC8Fra1wP0SHzKZbK11MrbVs"
    # PHONE_NUMBER = "+"
    ADMINS = [
        2056493966, 
    ]


bot = TelegramClient(
    session=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
).start()