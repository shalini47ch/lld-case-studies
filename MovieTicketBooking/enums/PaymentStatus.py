from enum import Enum

class PaymentStatus(Enum):
    PENDING=1
    CONFIRMED=2
    DECLINED=3
    REFUNDED=4