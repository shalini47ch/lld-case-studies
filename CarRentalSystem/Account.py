from abc import ABC,abstractmethod
from enums.AccountStatus import AccountStatus
from Person import Person

class Account(Person,ABC):
    def __init__(self,name,address,email,phone_number,account_id,password):
        super().__init__(name,address,email,phone_number)
        self.account_id=account_id
        self.password=password
        self.status=AccountStatus.NONE
        
    @abstractmethod
    def reset_password(self):
        pass
        
class Receptionist(Account):
    def __init__(self,name,address,email,phone_number,account_id,password,date_joined):
        super().__init__(name,address,email,phone_number,account_id,password)
        self.date_joined=date_joined
    
    