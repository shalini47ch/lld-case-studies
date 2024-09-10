#id,password,balance,status,person,hands

from abc import ABC,abstractmethod

class Player(ABC):
    def __init__(self,id,password,balance,status,person,hands):
        self.id=id
        self.password=password
        self.balance=balance
        self.status=status
        self.person=person
        self.hands=hands
    
    def addHand(self,hand):
        pass
    
    def removeHand(self,hand):
        pass
    
    def resetPassword(self):
        pass

#here we are inheriting the blackjackPlayer
class BlackJackPlayer(Player):
    def __init__(self,id,password,balance,status,person,hands,bet,totalCash):
        super().__init__(id,password,balance,status,person,hands)
        self.bet=bet
        self.totalCash=totalCash
    
    #create a helper function to place bet
    def placebet(self):
        pass
    
    def reset_password(self):
        pass

class Dealer(Player):
    def __init__(self,id,password,balance,status,person,hands):
        super().__init__(id,password,balance,status,person,hands)
    
    def get_total_score(self):
        pass
    
    def reset_password(self):
        pass
        
    

        
    

    