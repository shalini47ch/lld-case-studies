from abc import ABC,abstractmethod 

class Observer(ABC):
    @abstractmethod
    def update(self,message):
        pass

class Customer(Observer):
    def __init__(self,name):
        self.name=name
    
    def update(self,message):
        print(f"{self.name} received notification:{message}")

#now here creating the observable also called as subject 
class Subject:
    def __init__(self):
        self.observers=[]
    
    def add_observer(self,observer):
        self.observers.append(observer)
    
    #here create a helper function called as remove_observer
    def remove_observer(self,observer):
        self.observers.remove(observer)
    
    def notify(self,message):
        for observer in self.observers:
            observer.update(message)

if __name__=="__main__":
    subject=Subject()
    customer1=Customer("Alice")
    customer2=Customer("Bob")
    subject.add_observer(customer1)
    # subject.add_observer(customer2)
    subject.notify("Notification send to alice")

#so here we applied the observer design pattern