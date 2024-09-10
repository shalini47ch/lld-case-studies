#here we have the cards and the face values associated with them
#Ace has a face value of either 1 or 11,King Queen Jack have a face value of 10 and the other numbers will have the face value same as the number
class Card:
    def __init__(self,suit,faceValue):
        self.suit=suit
        self.faceValue=faceValue
    
    