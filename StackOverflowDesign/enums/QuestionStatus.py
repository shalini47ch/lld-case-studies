from enum import Enum

class QuestionStatus(Enum):
    #there are 4 steps to active,closed,flagged,bounty
    ACTIVE=1
    CLOSED=2
    FLAGGED=3
    BOUNTY=4
