#here we will create a class called as Order and will have parameters like orderid,status,meal,creationDate,table,waiter,chef
#status enum se lenge
from Meal import Meal
from enums.OrderStatus import OrderStatus
from Table import Table
#we will import the details of both the waiter as well as chef
from Person import Waiter,Chef
from datetime import datetime


class Order:
    def __init__(self,orderid,status,meal,creationDate,table,waiter,chef):
        self.orderid=orderid
        self.status=status
        self.meal=meal
        self.creationDate=creationDate if creationDate else datetime.now()
        self.table=table
        self.waiter=waiter
        self.chef=chef
    
    def __str__(self):
        return (f"Order(orderid={self.orderid}, status={self.status}, meal={self.meal}, "
                f"creationDate={self.creationDate}, table={self.table}, waiter={self.waiter}, chef={self.chef})")
        
#now here creating the main function
meal=Meal(1)
table=Table(12,"north","booked",6,4)
waiter=Waiter("ronit","ronit@gmail.com","8765432190","O11",datetime.now())
status=OrderStatus.PREPARED
chef=Chef("ronita","ronita@gmail.com","98765432109","O22",datetime.now())

order=Order(12,status,meal,None,table,waiter,chef)
print(order)
        
        