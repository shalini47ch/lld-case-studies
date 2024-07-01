#here we will use the factory design pattern to show the different types of notifications 
#we will create an abstract class for the notifications 

from abc import ABC,abstractmethod

class Notification(ABC):
    def __init__(self,content):
        self.content=content
    
    @abstractmethod
    def send(self,user):
        pass
#here we will have two types of notifications sms notification and email notification

class EmailNotification(Notification):
    def __init__(self,content):
        super().__init__(content)
    def send(self,user):
        print(f"Sending email to:{user.email}:{self.content}")
        #this helper function will help to send email notification
    
class SMSNotification(Notification):
    def __init__(self,content):
        super().__init__(content)
    def send(self,user):
        print(f"Sending sms to:{user.phone_number}:{self.content}")

#now here creating a notification factory to perform the notification
class NotificationFactory(Notification):
    @staticmethod
    def create_notification(notification_type,content):
        if(notification_type=="email"):
            return EmailNotification(content)
        elif(notification_type=="sms"):
            return SMSNotification(content)
        else:
            raise ValueError("Unknown notification type")
if __name__=="__main__":
    class User:
        def __init__(self,username,email,password,phone_number):
            self.username=username
            self.email=email
            self.password=password
            self.phone_number=phone_number
    #so here we created for the emailnotification type
    user=User("abcd","abc@gmail.com","123455678","789345677")
    email=NotificationFactory.create_notification("email","This is the content for email")
    email.send(user)
    
    #here we created for the smsnotification type
    sms=NotificationFactory.create_notification("sms","You have a new SMS")
    sms.send(user)
    
    