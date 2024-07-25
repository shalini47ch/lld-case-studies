#here we will create an account class that will have accountid,accountstatus,address,password
from enums.AccountStatus import AccountStatus
from Address import Address

class Account:
    def __init__(self,accountid,accountstatus,address,password):
        self.accountid=accountid
        self.accountstatus=accountstatus
        self.address=Address
        self.password=password
    
    def resetPassword(self):
        pass

        