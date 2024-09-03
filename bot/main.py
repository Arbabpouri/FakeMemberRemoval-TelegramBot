from telethon.types import PeerChannel, ChannelParticipantsSearch, User, PeerUser
from telethon.tl.types.channels import ChannelParticipants
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import NewMessage
from telethon.errors.rpcerrorlist import FloodWaitError, ChannelInvalidError, ChannelPrivateError
from telethon.custom import Message
from itertools import combinations
import asyncio
from config import Config, bot, ALL_CHARACTERS
from algoritms import Algoritms


cancel = False

def generate_combinations(characters):
    
    for i in range(1, len(characters) + 1):
        for combo in combinations(characters, i):
            yield ''.join(combo)
    

@bot.on(NewMessage(incoming=True, chats=Config.ADMINS, pattern="^check \d{8,15} [1-9]{1}\d{2,4}$"))
async def check_channel(event: Message) -> None:
    global cancel
    
    _, channel_id, users_num = str(event.message.message).split(' ')
    users_num = int(users_num)
    channel = PeerChannel(int(channel_id))
    users_removed = 0
    users_find = 0
    
    message = await event.reply("Please wait")
    
    
    try:
        
        await message.edit("Started")

        for combo in generate_combinations(ALL_CHARACTERS):
            
            response: ChannelParticipants = await bot(GetParticipantsRequest(channel=channel,filter=ChannelParticipantsSearch(combo), offset=0, limit=200, hash=0))
            
            if response.users:
                
                users_find += len(response.users)
                
                try:
                    for user in response.users:

                        if cancel:
                            cancel = False
                            print("Canceled")
                            return
                        
                        elif (user_check := Algoritms(user=user)) and user_check.check():
                            
                            if user_check.is_fake_name:
                                user_full = await bot(GetFullUserRequest(PeerUser(user.id)))
                                await asyncio.sleep(2)
                                if not user_full.full_user.about:
                                    continue
                            
                            await bot.kick_participant(entity=channel,user=user)
                            users_removed += 1
                        
                            await asyncio.sleep(1)
    
                except FloodWaitError as e:
                    text = f"flood wait error, please wait for {e.seconds} seconds"
                    await event.reply(text)
                    print(text)
                    await asyncio.sleep(e.seconds + 25)
                    print("End Flood Wait Error")
                    
                except Exception as e:
                    print("error,", e)
                    await event.reply(f"canceled, error : {e}")
                
                await message.delete()
                message = await event.reply(f"Now - All Users Find: {users_find} - Users Removed : {users_removed}")
                await asyncio.sleep(5)
                
            if users_find >= users_num:
                break
            
            await asyncio.sleep(10)        
        
    except (ChannelPrivateError, ChannelInvalidError):
        await event.respond("error, please admin me with full ticks or check your channel id")
            
    except Exception as e:
        print("error,", e)
        await event.reply(f"canceled, error : {e}")


@bot.on(NewMessage(from_users=Config.ADMINS, pattern='hello|cancel', incoming=True))
async def commands(event: Message) -> None:
    global cancel
    command = str(event.message.message)
    
    if command == "hello":
        await event.reply("Hello Welcome To Novin Member Checker Bot <3")
    elif command == "cancel":
        cancel = True
        await event.reply("Canceled")


if __name__ == "__main__":
    print("Bot is online")
    bot.run_until_disconnected()
    