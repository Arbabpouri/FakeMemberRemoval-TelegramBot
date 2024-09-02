from typing import Generator
from telethon.tl.types import User
class Algoritms:
    
    
    def __init__(self, user: User) -> None:
        self.user = user
        
        
    def deleted(self) -> bool:
        if self.user.deleted:
            return True
        return False
                
    def seen_time(self) -> bool:
        return True
        
        
        
    def check(self) -> bool:
        
        if self.deleted():
            return True
        elif self.seen_time():
            return True
        
        
        return False