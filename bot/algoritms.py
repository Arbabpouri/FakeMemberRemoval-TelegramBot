from typing import Generator
from telethon.tl.types import User, UserStatusLastMonth, UserStatusEmpty
class Algoritms:
    
    
    def __init__(self, user: User) -> None:
        self.user = user        
    
    @property
    def is_deleted(self) -> bool:
        
        if self.user.deleted:
            return True
        return False

    @property
    def last_seen_is_old(self) -> bool:
                
        if isinstance(self.user.status, (UserStatusLastMonth, UserStatusLastMonth)):
            return True
        return False
    
    @property
    def is_fake_name(self) -> bool:
        first_name = self.user.first_name if self.user.first_name else ""
        last_name = self.user.last_name if self.user.last_name else ""
        
        full_name = first_name + last_name
        
        if len(set(full_name)) > 1:
            return False
        return True
        
    def check(self) -> bool:
        print('=' * 50)
    
        result = (
            self.is_deleted or
            self.last_seen_is_old or
            self.is_fake_name
        )
        
        text = f"User With Name - {self.user.first_name} - And User ID : {self.user.id}"
        
        if result:
            print(text, "Kicked")
        else:
            print(text, "Saved")
            
        return result
        