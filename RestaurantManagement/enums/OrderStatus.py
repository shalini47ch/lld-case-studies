from enum import Enum

class OrderStatus(Enum):
    PREPARED=1
    PENDING=2
    COMPLETED=3
    CANCELLED=4