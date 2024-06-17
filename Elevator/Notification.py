#Here we will send a notification to display the floor at which the elevator arrives
#we will solve it using the observer design pattern
#here we will create an observer and there will be an observable that will help
from abc import ABC,abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self,message):
        pass

#now here we will create an observable with the functions like add_observer,remove_oberserver and notify observer
class Observable(ABC):
    def __init__(self):
        self.observers=[]
    
    def add_observer(self,observer):
        self.observers.append(observer)
    
    def remove_observer(self,observer):
        self.observers.remove(observer)
    
    def notify_observers(self,message):
        #here we need to notify them with the messages
        for observer in self.observers:
            observer.update(message)

#Here we will create Elevator observable that is the implementation of observable
class Elevator(Observable):
    def __init__(self):
        super().__init__()
        self.current_floor=0
    
    def move_floor(self,floor):
        self.current_floor=floor
        self.notify_observers(f"Elevator arrived at floor {floor}")

class Display(Observer):
    def update(self,message):
        print(f"Display updated with message:{message}")
    
elevator=Elevator()
display=Display()
#so here we are adding the observers
elevator.add_observer(display)
elevator.move_floor(5)

elevator.remove_observer(display)
elevator.move_floor(6)






