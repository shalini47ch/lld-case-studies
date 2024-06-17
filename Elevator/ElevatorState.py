from abc import ABC,abstractmethod

class ElevatorState(ABC):
    @abstractmethod
    def handle(self,elevator):
        pass

#The state are Idle,MovingUp,MovingDown
class MovingUp(ElevatorState):
    def handle(self,elevator):
        elevator.current_floor+=1
        print(f"Elevator is moving up to floor {elevator.current_floor}")

class MovingDown(ElevatorState):
    def handle(self,elevator):
        elevator.current_floor-=1
        print(f"Elevator is moving down to floor{elevator.current_floor}")
        
class Idle(ElevatorState):
    def handle(self,elevator):
        print(f"Elevator is idle at {elevator.current_floor}")

#now here we will set the state
class Elevator:
    def __init__(self):
        self.state=Idle()
        self.current_floor=12
    
    def set_state(self,state):
        self.state=state
    
    def handle(self):
        self.state.handle(self)
    
#now here we write the client code
elevator=Elevator()
elevator.handle()

elevator.set_state(MovingUp())
elevator.handle()

elevator.set_state(MovingDown())
elevator.handle()


