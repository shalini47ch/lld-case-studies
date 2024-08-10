from abc import ABC,abstractmethod 
from enums.AccountStatus import AccountStatus
from Address import Address

class Account(ABC):
    def __init__(self,id,password,accountStatus,address,email,phoneNumber):
        self.id=id
        self.password=password
        self.accountStatus=accountStatus
        self.address=address
        self.email=email
        self.phoneNumber=phoneNumber
    
    #here we will create the getter functions to get the address,email and phoneNumber
    def getAddress(self):
        return self.address
    
    def getEmail(self):
        return self.email
    
    def getPhoneNumber(self):
        return self.phoneNumber
    
    def reset_password(self):
        pass
    
        