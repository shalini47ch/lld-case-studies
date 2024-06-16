#here create enum for the elevator state
from enum import Enum

class ElevatorState(Enum):
    IDLE=1
    UP=2
    DOWN=3  
