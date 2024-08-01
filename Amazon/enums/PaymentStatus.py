from enum import Enum

class PaymentStatus(Enum):
    CONFIRMED=1
    DECLINED=2
    PENDING=3
    REFUNDED=4

