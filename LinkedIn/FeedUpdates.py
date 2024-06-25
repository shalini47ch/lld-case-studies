#Here in order to notify the users we will use the observer design pattern
#this follower is the observer that will receive the updates
class Follower:
    def __init__(self,name):
        self.name=name
    
    def receive_update(self,user_name,update):
        print(f"{self.name} received updates from {user_name}:{update}")
    
#now this is the observable
class User:
    def __init__(self,name):
        self.name=name
        self.followers=[]
    
    def follow(self,follower):
        self.followers.append(follower)
    
    def post_update(self,update):
        print(f"{self.name} posted: {update}")
        self.notify_followers(update)
    
    def notify_followers(self,update):
        for follower in self.followers:
            follower.receive_update(self.name,update)

user1=User("John Doe")
user2=User("Monita")
follower1=Follower("Follower 1 ")
follower2=Follower("Follower 2")
user1.follow(follower1)
user1.follow(follower2)
user1.post_update("Hello LinkedIn")     

#Here observer design pattern is used       
        
