from abc import ABC,abstractmethod 

class Service(ABC):
    def __init__(self,issuedAt):
        self.issuedAt=issuedAt
    
    @abstractmethod 
    def addVoiceItem(self):
        pass

#we will have amenity,roomservice,kitchen service
class Amenity(Service):
    def __init__(self,name,description):
        super().__init__(issuedAt)
        self.name=name
        self.description=description
    
    def addVoiceItem(self):
        pass

class RoomService(Service):
    def __init__(self,isChargable,requestTime):
        super().__init__(issuedAt)
        self.isChargable=isChargable
        self.requestTime=requestTime
        
    def addVoiceItem(self):
        pass

class KitchenService(Service):
    def __init__(self,description):
        super().__init__(issuedAt)
        self.description=description
    
    def addVoiceItem(self):
        pass

    
        
    
        
    


        
    
    