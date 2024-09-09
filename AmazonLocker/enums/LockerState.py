#here we will define an enum that shows the locker states like closed,booked,available
from enum import Enum

class LockerState(Enum):
    CLOSED=1
    BOOKED=2
    AVAILABLE=3