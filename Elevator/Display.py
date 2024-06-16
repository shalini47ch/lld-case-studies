class Display:
    def __init__(self,floor,capacity,direction):
        self.floor=floor
        self.capacity=capacity
        self.direction=direction
    
    def get_floor(self):
        return self.floor
    
    def set_floor(self,floor):
        self.floor=floor
    
    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self,capacity):
        self.capacity=capacity
    
    def get_direction(self):
        return self.direction
    
    def set_direction(self,dir):
        self.direction=dir
    
    def showElevatorDisplay(self):
        return f"The elevator is at Floor  {self.floor} has a capacity of {self.capacity} and direction of {self.direction}"
    
    def showhalldisplay(self):
        return f"The hall is at {self.floor} and the direction is {self.direction}"
    
    
    

    
    
        