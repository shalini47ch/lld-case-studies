class Address:
    def __init__(self,zip,address,city,country,state):
        self.zip=zip
        self.address=address
        self.city=city
        self.country=country
        self.state=state
    
    def getCity(self):
        return self.city
    
    def getCountry(self):
        return self.country
    
    def getState(self):
        return self.state