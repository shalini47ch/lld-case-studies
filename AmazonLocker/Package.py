from Order import Order

class Package:
    def __init__(self,packageId,packageSize,order):
        self.packageId=packageId
        self.packageSize=packageSize
        self.order=order
    
    def get_packageId(self):
        return self.packageId
    
    def get_packageSize(self):
        return self.packageSize
    
    def getOrder(self):
        print(f"order with order id {self.order.get_orderid()} has the following items {self.order.get_items()}")

order=Order("13",["mango","banana"],"india")
package=Package("123","L",order)

package.getOrder()
package.get_packageId()
package.get_packageSize()

#this is the package class that we will use in the locker and order is the one which will be imported from the other class

    
    