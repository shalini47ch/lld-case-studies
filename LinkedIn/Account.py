#status will be taken from enums folder
class Account:
    def __init__(self,status,accountId,username,password,email):
        self.accountId=accountId
        self.username=username
        self.password=password
        self.email=email
        
    #here create a helper function 
    def reset_password(self):
        pass

    
    
    
        