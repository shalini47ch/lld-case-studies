#here we create a class representing the notification of a locker 
class Notification:
    def __init__(self,customerid,orderid,lockerid,code):
        self.customerid=customerid
        self.orderid=orderid
        self.lockerid=lockerid
        self.code=code
    
    #now here we will create getter and the setter methods 
    def get_customer_id(self):
        return self.customerid
    
    def get_orderid(self):
        return self.orderid
    
    def get_lockerid(self):
        return self.lockerid
    
    def get_code(self):
        #this is a 6 digit code meant to open the locker
        return self.code
    
    #create one more helper function to send the notification
    def send(self):
        print("Notification to a specific customer is sent")

    

    
    
    
    