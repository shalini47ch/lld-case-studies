#here it will have parameters like name,city,country,zipcode,streetAddress,state

class Person:
    def __init__(self,name,city,country,zipcode,streetAddress,state):
        self.name=name
        self.city=city
        self.country=country
        self.zipcode=zipcode
        self.streetAddress=streetAddress
        self.state=state
    
    def getName(self):
        return self.name
    
    def getCity(self):
        return self.city
    
    def getCountry(self):
        return self.country
    
    def getZipCode(self):
        return self.zipcode
    
    def getstreetAddress(self):
        return self.streetAddress
    
    def getState(self):
        return self.state

#This game has a lot of states that can be handled by the state design pattern and even iterator can be used for next
