#here we will create a locker class that will represent individual lockers
#lockerid,lockersize,isAssigned,pin,observers
#here we will also use the observer design pattern that will send the notification with the lockerid and the pin 

class Locker:
    def __init__(self,lockerid,lockersize):
        self.lockerid=lockerid
        self.lockersize=lockersize
        self.isAssigned=False #this means the locker is not assigned to anyone
        self.pin=None
        self.observers=[]
    
    #it has two functions one when it is assigned and the other is when the item is picked up and is free
    def assign(self,pin):
        #here we will assign a locker to a customer with a specific pin and send the notification to the customer that the locker has been assigned
        self.isAssigned=True
        self.pin=pin
        self.notify_observers()
    
    def free(self):
        self.isAssigned=False
        self.pin=None
    #now here we will create helper functions like addobservers,removeobservers and notifyobservers
    
    def add_observers(self,observer):
        self.observers.append(observer)
    
    def remove_observers(self,observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.lockerid,self.pin)
    
    #create one more helper function to check for the validity of the pin whether the entered pin is valid or not
    def check_pin(self,pin):
        return self.isAssigned and self.pin==pin

#now the next one is to create a customer class and give the details of the update method
class Customer:
    def __init__(self,customerid,latitude,longitude):
        #here it has customerid,latitude,longitude,assignedlocker and pin
        self.customerid=customerid
        self.latitude=latitude
        self.longitude=longitude
        self.assigned_locker=None #this will store whether the locker is assigned or not
        self.pin=None #this variable will help to set the pin
    
    def update(self,lockerid,pin):
        self.assigned_locker=lockerid
        self.pin=pin
        print(f"Customer with { self.customerid} is assigned to a Locker:{self.assigned_locker} with a pin of {self.pin}")
    
    def unassign_locker(self,pin):
        if self.assigned_locker and self.assigned_locker.check_pin(pin)==pin:
            #here we will unassign the locker and the pin
            self.assigned_locker.free()
            self.assigned_locker=None
            self.pin=None
            print(f"Customer with {self.customerid} unassigned successfully")
            return True
        else:
            print(f"Customer with {self.customerid} :Invalid pin")
    
        
    
    
    

    
    
    
    