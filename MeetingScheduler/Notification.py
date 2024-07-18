#here we will use the observer design pattern to create a notification system
from abc import ABC,abstractmethod
from datetime import datetime

class Observer(ABC):
    @abstractmethod
    def update(self,message):
        pass

#here we will first create the observable
class Subject(ABC):
    def __init__(self):
        self.observers=[]
    
    #attach and detach are same like subscribe and unsubscribe
    def attach(self,observer):
        self.observers.append(observer)
    
    def detach(self,observer):
        self.observers.remove(observer)
    
    #similarly create a helper function to perform the notify me operation
    def notify(self,message):
        for observer in self.observers:
            observer.update(message)
class User:
    def __init__(self,userid,name,email):
        self.userid=userid
        self.name=name
        self.email=email

class UserObserver(Observer):
    def __init__(self,user):
        self.user=user
    
    def update(self,message):
        print(f"Notification sent to {self.user.email}:{message}")

#now here we will create a notification class inheriting frommthe subjects
class Notification(Subject):
    def __init__(self,notification_id,content,creation_date):
        #we will first inherit from the observers
        super().__init__()
        self.notification_id=notification_id
        self.content=content
        self.creation_date=creation_date
    #create two helper function one for send notification
    def send_notification(self):
        self.notify(f"Notification sent:{self.content}")
    
    def cancel_notification(self):
        self.notify(f"Notification cancelled:{self.content}")

user1=User(1,"alice","alice@gmail.com")
user2=User(2,"bob","bob@gmail.com")

userobserver1=UserObserver(user1) #here in the parameter we need to send our users
userobserver2=UserObserver(user2)

notification=Notification(1,"hello",datetime.now())
notification.attach(userobserver1)
notification.attach(userobserver2)

notification.send_notification()
notification.cancel_notification()

        
    
    
    
        
        
    