#create an abstractmethod

from abc import ABC,abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self,message,receipent):
        pass

#we will use two classes one is Email and the other is sms notification
class EmailNotification(Notification):
    def send(self,message,receipent):
        print(f"Sending email to {receipent}:{message}")
    
class SMSNotification(Notification):
    def send(self,message,receipent):
        print(f"Sending sms to {receipent}:{message}")

#now at last we will create a factory and on the type of message sent

class NotificationFactory:
    @staticmethod
    def create_notification(method):
        if(method=="email"):
            return EmailNotification()
        elif(method=="sms"):
            return SMSNotification()
        else:
            raise TypeError("Invalid message type added")
notification=NotificationFactory.create_notification("email")
notification.send("hello","user1@gmail.com")   

#here sending of notification is done by factory design pattern
 