from telethon import TelegramClient
from string import ascii_letters, digits

class Config:
    
    SESSION_NAME = "NovinMemberCheckerBot"
    API_ID = 10603708
    API_HASH = "f17d354888d912173f1599ca3133e04e"
    ADMINS = [
        2056493966, 
    ]


PERSIAN_CHARACTERS = [
    'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ',
    'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل',
    'م', 'ن', 'و', 'ه', 'ی'
]
    
ALL_CHARACTERS = list(ascii_letters) + list(digits) + PERSIAN_CHARACTERS

bot = TelegramClient(
    session=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
).start()