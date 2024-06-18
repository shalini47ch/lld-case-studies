#here we are implementing the algorithms to decide on the type of algorithms for the lift to move fcfs,scan,look,sstf
#here sstf stands for shortest seek time first

from abc import ABC,abstractmethod

#we will first write the algorithm for the fcfs (first come first serve) the first request to be added will be the first one to be removed
class ElevatorStrategy(ABC):
    @abstractmethod
    def schedule(self,requests,current_floor):
        pass
    
#here we create a helper function called as FCFSStrategy
class FCFSStrategy(ElevatorStrategy):
    def schedule(self,requests,current_floor):
        #this means if there are requests in the list
        return requests.pop(0) if requests else current_floor

#here creating another algorithm called as shortest seek time strategy
#the objective of this is to minimize the travel distance
class SSTFStrategy(ElevatorStrategy):
    def schedule(self,requests,current_floor):
        if not requests:
            return current_floor
        next_floor=min(requests,key=lambda x:abs(x-current_floor))
        requests.remove(next_floor)
        return next_floor

class Elevator:
    def __init__(self,strategy):
        self.strategy=strategy
        self.current_floor=0
        self.requests=[]
    
    def set_strategy(self,strategy):
        self.strategy=strategy
    
    def add_request(self,floor):
        self.requests.append(floor)
    
    def move(self):
        if self.requests:
            self.current_floor = self.strategy.schedule(self.requests, self.current_floor)
            print(f"Elevator moved to floor {self.current_floor}")
        else:
            print("No requests to process")

elevator=Elevator(FCFSStrategy())
elevator.add_request(3)
elevator.add_request(4)
elevator.add_request(5)
elevator.move()
elevator.move()
elevator.move()

print("**********************")

#similarly do it for shortest seek time first
elevator1=Elevator(SSTFStrategy())
elevator1.add_request(6)
elevator1.add_request(7)
elevator1.add_request(8)
elevator1.move()
elevator1.move()
elevator1.move()


        
    
    
    


        
    

