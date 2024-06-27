#this vehicle log type helps us to find the vehiclecurrent status
from enum import Enum

class VehicleLogType(Enum):
    ACCIDENT=1
    LOG=2
    FUELING=3
    REFILLING=4
    REPAIR=5