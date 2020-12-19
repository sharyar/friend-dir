from dataclasses import dataclass, field
from datetime import date, time, datetime



@dataclass
class Friend:
    fname : str = None
    lname : str = None
    phone : str = None
    birthdate: date = None
    
    
    def __post_init__(self):
        if self.birthdate != None:
            self.birthdate = date.fromisoformat(self.birthdate)
        self.last_contact = date.today()
            
    def __str__(self) -> str:
        return (f'{self.fname} {self.lname} - {self.phone}. '
                f'Born on {self.birthdate.strftime("%B-%d-%Y")}. ' 
                f'Last Contacted: {self.last_contact.strftime("%B-%d-%Y")}.')
        
    def set_last_contacted_date(self, date_contact = date.today()):
        self.last_contact = date_contact
        
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Friend):
            raise ValueError('Can not compare a non-friend object')
        
        return (self.fname == o.fname and self.lname == o.lname and self.birthdate == o.birthdate)
            

class FriendList:
    def __init__(self, friends = []) -> None:
        super().__init__()
        self.friends = friends
        
    def add_friend_to_list(self, friend):
        if friend in self.friends:
            print('A duplicate may exist. Please check list first.')
        else: 
            self.friends.append(friend)
    
    def delete_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            print('Deleted')
            
    def __str__(self) -> str:
        return str(list(friend.fname + ' ' + friend.lname for friend in self.friends))
        

f1 = Friend('Sam', 'Hurd', '780-293-2379', '2020-01-01')
print(f1)
f2 = Friend('Sam', 'Hurd', '780-293-2379', '2020-01-01')
print(f2)

list_friends = FriendList([f1, f2])
print(list_friends)
