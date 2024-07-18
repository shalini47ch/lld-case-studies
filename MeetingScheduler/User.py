class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    
    def get_name(self):
        return self.name 
    
    def get_email(self):
        return self.email
    
    def respondInvitation(self):
        pass #this will keep track of whether to accept or reject the notification
    
    