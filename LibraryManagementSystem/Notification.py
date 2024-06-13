from abc import ABC,abstractmethod
from UserManagement import Member
from datetime import date


#here we will send a notification to the member indicating that due is tomorrow
#here observer design pattern added
#This is the observer
class Notification(ABC):
    @abstractmethod
    def notify(self):
        pass
#These are the concrete observers
class EmailNotification(Notification):
    def notify(self,message):
        print(f"Sending email notification:{message}")

#similarly sending the SMSNotification
class SMSNotification(Notification):
    def notify(self,message):
        print(f"Sending sms notification:{message}")

class NotifiableMember(Member):
    def __init__(self,userid,name,email,date_of_membership):
        super().__init__(userid,name,email,date_of_membership)
        self.notifications=[]
    
    def add_notification(self,notification):
        self.notifications.append(notification)
    
    def notify(self,message):
        for notification in self.notifications:
            notification.notify(message)

#implementing the client code 
member=NotifiableMember(12,"annie","annie@gmail.com",date.today())
member.add_notification(EmailNotification())
member.add_notification(SMSNotification())
member.notify("Your book is due for tomorrow")


        
        

