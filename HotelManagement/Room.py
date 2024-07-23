from enums.RoomStatus import RoomStatus
from enums.RoomStyle import RoomStyle


class Room:
    def __init__(self,roomNo,style,status,bookingPrice,isSmoking):
        self.roomNo=roomNo
        self.style=RoomStyle
        self.status=RoomStatus
        self.bookingPrice=bookingPrice
        self.isSmoking=isSmoking
    
    def isRoomAvailable(self):
        if(self.status=="AVAILABLE"):
            return True
        return False
    
    def checkIn(self):
        pass
    def checkOut(self):
        pass

    
        