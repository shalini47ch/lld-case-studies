#here we will use the status from the enums folder
from enums.AccountStatus import AccountStatus
class Account:
    def __init__(self,accountid,username,password,name,email,phone,status):
        self.accountid=accountid
        self.username=username
        self.password=password
        self.name=name
        self.email=email
        self.phone=phone
        #self.status=AccountStatus
    
    def reset_password(self):
        pass

        