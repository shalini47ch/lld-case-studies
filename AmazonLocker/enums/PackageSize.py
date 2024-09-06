#the packages that needs to be picked up from the locker will have three sizes as small medium and large
from enum import Enum

class PackageSize(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3