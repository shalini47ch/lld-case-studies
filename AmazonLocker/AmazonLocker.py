#here we will apply the singleton design pattern
from Strategylocation import DistanceCalculationStrategy,EucledianDistance
import random
import sys
class AmazonLockerSystem:
    _instance=None
    def __new__(cls, strategy):
        if cls._instance is None:
            #means here we will create a new instance
            cls._instance=super().__new__(cls)
            cls._instance.locations=[]
            cls._instance.strategy=strategy
        return cls._instance
    
    def add_location(self,location):
        self.locations.append(location)
    
    #here create a helper function to find the closest location of the person to the locker
    def find_closest_location(self,customerlati,customerlongi):
        closestlocation=None
        mindistance=sys.maxsize
        #iterate through the locations
        for location in self.locations:
            distance=self.strategy.calculate(location.latitude,location.longitude,customerlati,customerlongi)
            #now we will check if the distance is less than the minimum distance then we will update
            if(distance<mindistance):
                mindistance=distance
                closestlocation=location
        return closestlocation
    
    def assign_locker(self, customer, package_size) -> bool:
        closest_location = self.find_closest_location(customer.latitude, customer.longitude)
        if closest_location:
            for locker in closest_location.lockers:
                if not locker.isAssigned and locker.lockersize == package_size:
                    pin = random.randint(100000, 999999)
                    locker.assign(pin)
                    customer.assigned_locker = locker
                    customer.pin = pin
                    locker.add_observers(customer)
                    return True
        return False

    
            
        
        
    
    
            
            
    
    
    