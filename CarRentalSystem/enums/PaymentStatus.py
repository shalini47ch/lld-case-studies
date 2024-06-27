from enum import Enum

class PaymentStatus(Enum):
    UNPAID=1
    PENDING=2
    PAID=3
    CANCELLED=4
    REFUNDED=5


    