from enum import Enum

#Active,closed,cancelled,blacklisted,None

class AccountStatus(Enum):
    ACTIVE=1
    CLOSED=2
    CANCELLED=3
    BLACKLISTED=4
    NONE=5

    