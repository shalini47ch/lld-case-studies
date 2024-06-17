from enums.door import DoorStatus
from Display import Display
from enums.direction import Direction

class Door:
    def __init__(self,state):
        self.state=state
    
    #now create two helper functions to check for isOpen() state and the other is to check the state
    def isOpen(self):
        return self.state
    
    def set_state(self,state):
        self.state=state

#similarly do it for floor
class Floor:
    def __init__(self,floor_number,total_floor,display,panel):
        self.floor_number=floor_number
        self.total_floor=total_floor
        self.display=display
        self.panel=panel
    
    def is_bottommost(self):
        return self.floor_number==1
    
    #create a helper function to find the top most floor
    def topmost_floor(self):
        #so this indicates that we are in the top floor or not
        return self.floor_number==self.total_floor
    #now here implementing the getters to get the floor numbers
    def get_floor_number(self):
        return self.floor_number
    
    def get_total_floor(self):
        return self.total_floor
    
    def get_display(self):
        return self.display
    
    def get_panel(self):
        return self.panel

display=Display(1,None,Direction.UP)
panel="Some data"
floor=Floor(1,10,display=display,panel=panel)
print(floor.is_bottommost())
print(floor.get_floor_number())
print(floor.topmost_floor())

#here similarly we will check for the door
door=Door(DoorStatus.OPEN)
print(door.isOpen())
door.set_state(DoorStatus.CLOSED)


    
    
        
        
    

    

        