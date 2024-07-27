#here we will create a class called as Table  that will have different parameters like tableid,location,status,maxCapacity,seats i.e the no of seats 
#status will be an enum which you will inherit later from the enum folder  and seats will be a list
class Table:
    def __init__(self,tableid,maxCapacity):
        self.tableid=tableid
        self.maxCapacity=maxCapacity
        
    
    def add_reservation(self):
        print("reservation added")


        