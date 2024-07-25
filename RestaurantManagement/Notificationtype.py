#here to define the type of notification we will use the factory design pattern
from abc import ABC,abstractmethod 

class Notification(ABC):
    @abstractmethod 
    def send(self,receipent,message):
        pass
#now here we will create two child classes called as the SMSNotification and the other is called as EmailNotification

class SMSNotification(Notification):
    def send(self,receipent,message):
        print(f"SMS sent to {receipent}:{message}")

#similarly do it for EmailNotification
class EmailNotification(Notification):
    def send(self,receipent,message):
        print(f"EmailNotification sent to {receipent}:{message}")
    
#now here we will create a notification factory and then create a helper function called as create_notification
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if(notification_type=="SMS"):
            return SMSNotification()
        elif(notification_type=="EMAIL"):
            return EmailNotification()
        else:
            raise ValueError(f"Unknown notification type:{notification_type}")
if __name__=="__main__":
    factory=NotificationFactory()
    sms_notification=factory.create_notification("SMS")
    sms_notification.send("+89765431498","Table is booked")
    
    email_notification=factory.create_notification("EMAIL")
    email_notification.send("abc@gmail.com","Table is booked")
    
    
    
    
        

