from enum import Enum

class PaymentStatus(Enum):
    UNPAID=1
    PENDING=2
    COMPLETED=3
    DECLINED=4
    SETTLED=5
    REFUNDED=6
