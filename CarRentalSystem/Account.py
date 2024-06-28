from abc import ABC,abstractmethod
from enums.AccountStatus import AccountStatus
from Person import Person
from datetime import datetime

class Account(Person,ABC):
    def __init__(self,name,address,email,phone_number,account_id,password):
        super().__init__(name,address,email,phone_number)
        self.account_id=account_id
        self.password=password
        self.status=AccountStatus.ACTIVE
        
    @abstractmethod
    def reset_password(self):
        pass
        
class Receptionist(Account):
    def __init__(self,name,address,email,phone_number,account_id,password,date_joined):
        super().__init__(name,address,email,phone_number,account_id,password)
        self.date_joined=date_joined
    
    def search_customer(self,name):
        print(f"Searching customer with a name:{name}")
    
    
    def add_reservation(self):
        print("Adding a reservation")
    
    def cancel_reservation(self):
        print("Cancelling a reservation")
    
    def reset_password(self):
        print("Resetting the password of receiptionist")
        

class Customer(Account):
    def __init__(self,name,address,email,phone_number,account_id,password,license_number,license_expiry):
        super().__init__(name,address,email,phone_number,account_id,password)
        self.license_number=license_number
        self.license_expiry=license_expiry
    
    def add_reservation(self):
        print(f"Adding a reservation for the customer")
    
    def cancel_reservation(self):
        print(f"Cancelling reservation for the customer")
    
    def get_reservation(self):
        print("Getting reservation for customer")
    
    def reset_password(self):
        print("Resetting the password for the customer")

receptionist=Receptionist("abc","Mumbai","abc@gmail.com","8956789909","12","dfgtrey",datetime.now())
receptionist.search_customer("john")
receptionist.add_reservation()
receptionist.cancel_reservation()
receptionist.reset_password()
        
    


    
    
    
    
    
    