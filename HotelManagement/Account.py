from AccountStatus import AccountStatus
class Account:
    def __init__(self,id,password,status):
        self.id=id
        self.password=password
        self.status=AccountStatus.ACTIVE
        
    
    def reset_password(self):
        pass




        