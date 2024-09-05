class Order:
    def __init__(self,orderId,items,deliveryLocation):
        self.orderId=orderId
        self.items=items
        self.deliveryLocation=deliveryLocation
        
    #now here we will create the getter and the setter functions
    def get_orderid(self):
        return self.orderId
    
    def get_items(self):
        return self.items
    
    def get_delivery_location(self):
        return self.deliveryLocation
