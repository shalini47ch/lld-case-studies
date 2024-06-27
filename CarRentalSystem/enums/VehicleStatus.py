from enum import Enum

class VehicleStatus(Enum):
    AVAILABLE=1
    RESERVED=2
    LOST=3
    BEING_SERVICED=4