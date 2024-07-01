class Bounty:
    def __init__(self,reputationPoints,expiryDate):
        self.reputationPoints=reputationPoints
        self.expiryDate=expiryDate
    
    def updateReputationPoints(self,newpoints):
        self.reputationPoints=newpoints
    
