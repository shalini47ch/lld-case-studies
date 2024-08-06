class Address:
    def __init__(self,zip,address,city,country,state):
        self.zip=zip
        self.address=address
        self.city=city
        self.country=country
        self.state=state
    
    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}, {self.zip} {self.address}"
    
    def getCity(self):
        return self.city
    
    def getCountry(self):
        return self.country
    
    def getState(self):
        return self.state