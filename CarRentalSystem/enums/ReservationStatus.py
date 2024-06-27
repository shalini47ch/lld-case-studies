from enum import Enum

class ReservationStatus(Enum):
    #active,pending,confirmed,completed,cancelled
    ACTIVE=1
    PENDING=2
    CONFIRMED=3
    COMPLETED=4
    CANCELLED=5