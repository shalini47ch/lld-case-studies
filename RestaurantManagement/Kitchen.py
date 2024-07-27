#here it will have two parameters name and chef and will have a function called as assignChef()
from Chef import Chef

class Kitchen:
    #here we will inherit the chef from another class called as chef
    def __init__(self,name,chef):
        self.name=name #this will store the name of the kitchen
        self.chef=Chef #this will store the chef assigned for that kitchen
    
    def assignChef(self):
        pass
    
    
    
