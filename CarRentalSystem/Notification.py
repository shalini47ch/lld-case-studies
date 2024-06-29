#this notification will also use the factory design pattern
from abc import ABC,abstractmethod
from datetime import datetime


class Notification(ABC):
    def __init__(self,notification_id,created_on,content):
        self.notification_id=notification_id
        self.created_on=created_on
        self.content=content
    
    @abstractmethod
    def send_notification(self,message):
        pass

#here there are  sms and email notification
class SMSNotification(Notification):
    def __init__(self,notification_id,created_on,content):
        super().__init__(notification_id,created_on,content)
        
    def send_notification(self,account):
        print(f"Sending SMS to account {account}:{self.content}")
    
class EmailNotification(Notification):
    def __init__(self,notification_id,created_on,content):
        self.notification_id=notification_id
        self.created_on=created_on
        self.content=content
        
    def send_notification(self,account):
        print(f"Sending email to account{account}:{self.content}")

#Now here creating a factory to decide the type of notification you need
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type,notification_id,created_on,content):
        if(notification_type=="SMS"):
            return SMSNotification(notification_id,created_on,content)
        elif(notification_type=="EMAIL"):
            return EmailNotification(notification_id,created_on,content)
        else:
            raise TypeError("Unknown Notification Type")
#here creating an account class to keep track of the account
class Account:
    def __init__(self,identifier):
        self.identifier=identifier

#now here at last creating the main function
if __name__=="__main__":
    notification_id=1
    created_on=datetime.now()
    content="This is a test notification"
    account=Account("Account123")
    smsnoti=NotificationFactory.create_notification("SMS",notification_id,created_on,content)
    smsnoti.send_notification(account.identifier)
    
    #now similarly do it for Email notification as well
    emailnoti=NotificationFactory.create_notification("EMAIL",notification_id,created_on,content)
    emailnoti.send_notification(account.identifier)
    
    
    


    

        

