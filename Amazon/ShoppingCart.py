#this is similar to the cart we find in our ecommerce website

class ShoppingCart:
    def __init__(self,totalprice,items):
        self.totalprice=totalprice
        self.items=items
    
    def addItems(self,item):
        self.items.append(item)
    
    def removeItems(self,item):
        self.items.remove(item)
    
    def getItems(self):
        return self.items
    
    def checkOut(self):
        print("Checkout of the shopping cart")

cart=ShoppingCart(123,[])
cart.addItems("Apple")
cart.addItems("Mango")
cart.addItems("Banana")
cart.removeItems("Mango")
print(cart.getItems())



        