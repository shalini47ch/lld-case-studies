#we will first create a button class that represents an abstract class called as Button and has an abstract method called as is_pressed
from abc import ABC,abstractmethod

class Button(ABC):
    def __init__(self,status=False):
        self.status=status
    
    def press_down(self):
        self.status=True
    
    @abstractmethod
    def is_pressed(self):
        pass
    
    def get_status(self):
        return self.status
    
    def reset_status(self):
        self.status=False
    
#here there are two types of classes that will implement the button one is the hallbutton and the other is the elevator 
class HallButton(Button):
    def __init__(self,button_sign,status=False):
        super().__init__(status)
        #button sign indicates the sign of the button in hall
        self.button_sign=button_sign
    
    def is_pressed(self):
        return self.get_status()
    
    def get_buttonsign(self):
        return self.button_sign

#similarly do it for elevatorButton
class ElevatorButton(Button):
    def __init__(self,destination_floor,status=False):
        #inherit from the abstract class
        super().__init__(status)
        self.destination_floor=destination_floor
    
    def is_pressed(self):
        return self.get_status()
    
    def destination_floor(self):
        return self.destination_floor


    
        