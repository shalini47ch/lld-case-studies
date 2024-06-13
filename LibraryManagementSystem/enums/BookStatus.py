from enum import Enum

class BookStatus(Enum):
    AVAILABLE=1
    RESERVED=2
    LOANED=3
    LOST=4

    