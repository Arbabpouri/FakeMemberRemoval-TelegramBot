from telethon.types import PeerChannel, ChannelParticipantsSearch, User
from telethon.tl.types.channels import ChannelParticipants
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.events import NewMessage
from telethon.errors.rpcerrorlist import FloodWaitError, ChannelInvalidError, ChannelPrivateError
from telethon.custom import Message
from itertools import combinations
from string import ascii_letters, digits
import asyncio
from config import Config, bot
from algoritms import Algoritms



PERSIAN_CHARACTERS = [
    'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ',
    'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل',
    'م', 'ن', 'و', 'ه', 'ی'
]



def generate_combinations(characters):
    
    for i in range(1, len(characters) + 1):
        for combo in combinations(characters, i):
            yield ''.join(combo)
    



@bot.on(NewMessage(incoming=True, chats=Config.ADMINS, pattern="^check \d{8,15} [1-9]{1}\d{2,4}$"))
async def check_channel(event: Message) -> None:
    
    _, channel_id, users_num = str(event.message.message).split(' ')
    channel = PeerChannel(int(channel_id))
    users_removed = 0
    users_find = 0
    ALL_CHARACTERS = list(ascii_letters) + list(digits) + PERSIAN_CHARACTERS 
    
    message = await event.reply("Please wait")
    
    
    try:

        for combo in generate_combinations(ALL_CHARACTERS):
            
            response: ChannelParticipants = await bot(GetParticipantsRequest(channel=channel,filter=ChannelParticipantsSearch(combo), offset=0, limit=200, hash=0))
            
            if response.users:
                
                users_find += len(response.users)
                
                try:
                    for user in response.users:
                        
                        if Algoritms(user=user).check():
                            
                            await bot.kick_participant(entity=channel,user=user)
                            users_removed += 1
                        
                        await asyncio.sleep(1)
    
                except FloodWaitError as e:
                    text = f"flood wait error, please wait for {e.seconds} seconds"
                    await event.reply(text)
                    print(text)
                    await asyncio.sleep(e.seconds + 25)
                    print("End Flood Wait Error")
                    
                await message.edit(f"Now - All Users Find: {users_find} - Users Removed : {users_removed}")
                
            if users_num > users_num:
                break
            
            await asyncio.sleep(1)        
        
    except (ChannelPrivateError, ChannelInvalidError):
        await event.respond("error, please admin me with full ticks or check your channel id")
            
    except Exception as e:
        print("error,", e)


@bot.on(NewMessage(from_users=Config.ADMINS, pattern='hello', incoming=True))
async def start(event: Message) -> None:
    await event.reply("Hello Welcome To Novin Member Checker Bot <3")


if __name__ == "__main__":
    print("Bot is online")
    bot.run_until_disconnected()
    