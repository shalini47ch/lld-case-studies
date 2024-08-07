
from enums.ShippingStatus import ShippingStatus
from datetime import datetime
class ShipmentLog:
    def __init__(self,shipmentnumber,creationdate,status):
        self.shipmentnumber=shipmentnumber
        self.creationdate=creationdate
        self.status=status
    
    def get_shipmentNumber(self):
        return self.shipmentnumber
    
    def get_creationdate(self):
        return self.creationdate
    
    def get_status(self):
        return self.status
    
    def __str__(self):
        return f"ShipmentLog(shipmentnumber={self.shipmentnumber}, creationdate={self.creationdate}, status={self.status})"

#calling the main function
log=ShipmentLog(12,datetime.now(),ShippingStatus.PENDING)
print(log.get_shipmentNumber())
print(log.get_creationdate())
print(log)



        
        
        
        