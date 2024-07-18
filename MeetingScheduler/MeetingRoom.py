#here we will have parameters like id,capacity,bookedIntervals,isAvailable
class MeetingsRoom:
    def __init__(self,id,capacity,bookedIntervals,isAvailable):
        self.id=id
        self.capacity=capacity
        self.bookedIntervals=[]
        self.isAvailable=isAvailable #this is a boolean value to check if the meeting room is available or not
    
    