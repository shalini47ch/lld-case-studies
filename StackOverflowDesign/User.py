from Badge import Badge
class User:
    def __init__(self,reputationPoints,badges):
        self.reputationPoints=reputationPoints
        self.badges=Badge
        
    #here we create helper functions used by users
    def createQuestion(self):
        pass
    
    def addAnswer(self):
        pass
    
    def createComment(self):
        pass
    
    #now also adding the upvote and the downvote functionality
    def upvote(self,id):
        pass
    
    def downvote(self,id):
        pass
    
    def flagQuestion(self,question):
        pass
    
    def flagAnswer(self,answer):
        pass
    
    def voteToCloseQuestion(self,question):
        pass
    
    def voteToDeleteQuestion(self,question):
        pass
    
    def acceptAnswer(self,answer):
        pass

#there are two classes which will inherit from the User
class Admin(User):
    def __init__(self,reputationPoints,badges):
        super().__init__(reputationPoints,badges)
    
    def blockUser(self,user):
        pass
    
    def unblockUser(self,user):
        pass
    
    #so what happens here is that we assign a badge to the user
    def assignBadge(self,user,badge):
        pass 

class Moderator(User):
    def __init__(self,reputationPoints,badges):
        super().__init__(reputationPoints,badges)
    
    def closeQuestion(self,question):
        pass
    
    def reopenQuestion(self,question):
        pass
    
    def deleteQuestion(self,question):
        pass
    
    def restoreQuestion(self,question):
        pass
    
    def deleteAnswer(self,delete):
        pass

    
    

        

        