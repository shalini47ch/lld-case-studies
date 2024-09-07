#here we will use the eucledian distance strategy and manhatten distance  to find the location where we can assign lockers
from abc import ABC,abstractmethod
import math


class DistanceCalculationStrategy(ABC):
    def calculate(self,x1,y1,x2,y2):
        pass

#first calculate it using eucleadian distance and the other is manhatten distance

class EucledianDistance(DistanceCalculationStrategy):
    def calculate(self,x1,y1,x2,y2):
        return math.sqrt((x1 - x2)**2+(y1 - y2)**2)

class ManhattenDistance(DistanceCalculationStrategy):
    def calculate(self,x1,y1,x2,y2):
        return abs(x1-x2)+abs(y1-y2)
    
    
