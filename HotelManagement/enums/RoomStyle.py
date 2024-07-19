#here the room types are basically standard,delux,business suite and family suite
from enum import Enum

class RoomStyle(Enum):
    STANDARD=1
    DELUXE=2
    BUSINESSSUITE=3
    FAMILYSUITE=4