#here we will create an abstract class called as Person
from abc import ABC,abstractmethod 
from Address import import Address
from enums.AccountType import AccountType

#this person here is an abstract class
class Person(ABC):
    def __init__(self,name,address,email,phoneNumber,accountType):
        self.name=name
        self.address=Address
        self.email=email
        self.phoneNumber=phoneNumber
        self.accountType=AccountType
    
#Server,receiptionist,housekeeper and guest
#so here the server is inheriting from the Person
class Server(Person):
    def __init__(self,name,address,email,phoneNumber,accountType):
        super().__init__(name,address,email,phoneNumber,accountType)
    
    def addRoomCharge(self):
        pass

#now next we will create for the receiptionist that will have the functionality of create booking 
class Receiptionist(Person):
    def __init__(self,name,address,email,phoneNumber,accountType):
        super().__init__(name,address,email,phoneNumber,accountType)
    
    def createBooking(self):
        pass
#here creating another one inheriting that is the houseKeeping and the functionality assignToRoom

class HouseKeeping(Person):
    def __init__(self,name,address,email,phoneNumber,accountType):
        super().__init__(name,address,email,phoneNumber,accountType)
    
    def assignToRoom(self):
        #here basically housekeeping will be assigned to a specific room
        pass

class Guest(Person):
    def __init__(self,name,address,email,phoneNumber,accountType,totalRoomsCheckedIn):
        super().__init__(name,address,email,phoneNumber,accountType)
        self.totalRoomsCheckedIn=totalRoomsCheckedIn

    
    
    


        
    