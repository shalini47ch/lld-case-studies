#here the room status would be available,occupied,serviced,not reserved,others
from enum import Enum

class RoomStatus(Enum):
    AVAILABLE=1
    OCCUPIED=2
    SERVICED=3
    NOTRESERVED=4
    OTHERS=5
