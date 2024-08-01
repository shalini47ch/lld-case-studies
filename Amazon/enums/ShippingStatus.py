#pending,shipped,delivered,onhold

from enum import Enum

class ShippingStatus(Enum):
    PENDING=1
    SHIPPED=2
    DELIVERED=3
    ONHOLD=4
