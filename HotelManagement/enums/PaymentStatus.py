#when we are performing hotel booking there can be various payment methods like unpaid,pending,completed,failed,delclined,cancelled,refunded
from enum import Enum

class PaymentStatus(Enum):
    UNPAID=1
    PENDING=2
    COMPLETED=3
    FAILED=4
    DECLINED=5
    CANCELLED=6
    REFUNDED=7
