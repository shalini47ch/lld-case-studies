#here we will have two types of customers one is the Authenticated Customer and the other is the guestcustomer

from abc import ABC,abstractmethod 
from ShoppingCart import ShoppingCart
from Order import Order

class Customer(ABC):
    def __init__(self,cart):
        self.cart=ShoppingCart()
    
    @abstractmethod
    def getShoppingCart(self):
        pass

class Guest(Customer):
    def registerAccount(self):
        pass
    
    def getShoppingCart(self):
        return self.cart

class AuthenticatedCustomer(Customer):
    def __init__(self,cart):
        super().__init__()
        self.order=Order()
    
    def getShoppingCart(self):
        return self.cart


        
    

    