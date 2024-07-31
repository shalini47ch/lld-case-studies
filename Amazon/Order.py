
from enums.OrderStatus import OrderStatus
from ShoppingCart import ShoppingCart
from datetime import datetime
class Order:
    def __init__(self,orderNumber,OrderStatus,orderDate,orderlog,shoppingCart):
        self.orderNumber=orderNumber
        self.OrderStatus=OrderStatus
        self.orderDate=orderDate
        self.orderlog=orderlog
        self.shoppingCart=shoppingCart
    
    
    #now here creating three helper functions one for sendforShipment,makePayment,addOrderLog
    def sendforShipment(self):
        if(self.OrderStatus==OrderStatus.PAID):
            self.OrderStatus=OrderStatus.SHIPPED
            self.addOrderLog("Order sent for shipment")
            print("Order sent for shipment")
        else:
            print("Order cannot be shipped,payment pending")
    
    def makePayment(self,payment):
        #here check the status of the payment 
        if(self.OrderStatus==OrderStatus.PENDING):
            self.OrderStatus=OrderStatus.PAID
            self.addOrderLog(f"Payment {payment} made successfully")
            print("Payment made successfully")
        else:
            print("Payment cannot be made")
    
    def addOrderLog(self,log):
        self.orderlog.append(log)
        print(f"Order log updated {log}")

shopping_cart = ShoppingCart(123,[])  # Instantiate a ShoppingCart object
order_log = []
order = Order(orderNumber=12345, 
                  OrderStatus=OrderStatus.PENDING, 
                  orderDate=datetime.now(), 
                  orderlog=order_log, 
                  shoppingCart=shopping_cart)
    
# Make a payment
order.makePayment(100.00)

# Send the order for shipment
order.sendforShipment()

        
        