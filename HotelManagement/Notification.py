#here we will have two types of notifications called as SMS Notification and Email Notification
from abc import ABC,abstractmethod 

class Notification(ABC):
    @abstractmethod
    def send(self,receipent,message):
        pass

#here we will create SMSNotification and EmailNotification and then apply the factory design pattern
class SMSNotification(Notification):
    def send(self,receipent,message):
        print(f"Sending SMS TO {receipent}:{message}")
    
class EmailNotification(Notification):
    def send(self,receipent,message):
        print(f"Sending Email to {receipent}:{message}")

#now here creating a notification factory
class NotificationFactory:
    @staticmethod 
    def create_notification(notification_type):
        if(notification_type=="sms"):
            return SMSNotification()
        elif(notification_type=="email"):
            return EmailNotification()
        else:
            raise ValueError(f"Unknown notification type:{notification_type}")
#now perform the calling for the functions 
factory=NotificationFactory()
sms=factory.create_notification("sms")
email=factory.create_notification("email")
sms.send("+45677890321","Your room is ready to check in")
email.send("guest@gmail.com","Your booking has been confirmed")
    

