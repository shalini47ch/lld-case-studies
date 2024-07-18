#Here we will apply the strategy for the different types of notification system

from abc import ABC,abstractmethod

#here we have created a different notificationstrategy abstract class
class NotificationStrategy(ABC):
    @abstractmethod 
    def send(self,message,receipent):
        pass

#here we will have the email and the sms strategy
class EmailNotificationStrategy(NotificationStrategy):
    def send(self,message,receipent):
        print(f"Email sent to {receipent.name}:{message}")
        #here we have defined an email sent to the receipent

#similarly do it for SMSNotificationStrategy
class SMSNotificationStrategy(NotificationStrategy):
    def send(self,message,receipent):
        print(f"SMS sent to {receipent.name}:{message}")

class User:
    def __init__(self,userid,name,email,phonenumber):
        self.userid=userid
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
    
#here we will create a notification context and then set the strategy
class NotificationContext:
    def __init__(self,strategy):
        self.strategy=strategy
    def set_strategy(self,strategy):
        self.strategy=strategy
    
    def notify(self,message,receipent):
        self.strategy.send(message,receipent)

user1=User(1,"alice","alice@example.com",8945677890)
user2=User(2,"bob","bob@example.com",8345678908)

#creating the object for the notificationstrategy and sms strategy
emailnotifier=EmailNotificationStrategy()
smsnotifier=SMSNotificationStrategy()

context=NotificationContext(emailnotifier)
context.notify("Meeting Reminder",user1) #here once you have notified

#here we are having the notification strategy
context.set_strategy(smsnotifier)
context.notify("Sending meeting reminder through text",user2)




    