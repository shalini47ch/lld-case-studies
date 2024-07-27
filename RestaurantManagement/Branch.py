#branch has name,location,kitchen menu
from Kitchen import Kitchen 
from Menu import Menu

class Branch:
    def __init__(self,name,location,kitchen,menu):
        self.name=name
        self.location=location
        self.kitchen=kitchen
        self.menu=Menu
    
    def addSeatingChart(self):
        pass

        
