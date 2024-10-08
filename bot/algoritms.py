from telethon.tl.types import User, UserStatusLastMonth
from config import ALL_CHARACTERS

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
        
        if len(set(full_name.lower())) < 2 and full_name in ALL_CHARACTERS:
            return True
        return False
    
    @property
    def is_fake(self) -> bool:
        return self.user.fake
        
    def check(self) -> bool:
    
        result = (
            self.is_deleted or
            self.last_seen_is_old or
            self.is_fake_name or
            self.is_fake
        )
        
        text = f"User With Name - {self.user.first_name} - And User ID : {self.user.id}"
        
        if result:
            print(text, "Kicked")
        else:
            print(text, "Saved")
            
        return result
        