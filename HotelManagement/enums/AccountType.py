#Member,Guest,Manager,Receiptionist
from enum import Enum

class AccountType(Enum):
    MEMBER=1
    GUEST=2
    MANAGER=3
    RECEIPTIONIST=4
