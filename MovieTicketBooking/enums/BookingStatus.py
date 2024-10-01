from enum import Enum

class BookingStatus(Enum):
    PENDING=1
    CONFIRMED=2
    CANCELLED=3
    DENIED=4
    REFUNDED=5