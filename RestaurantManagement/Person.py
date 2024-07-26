from abc import ABC,abstractmethod 
from datetime import datetime

class Person(ABC):
    def __init__(self,name,email,phonenumber):
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.name} (email: {self.email}, phone: {self.phonenumber})"
    
#now we will have two classes that will inherit one will be the Customer and the other will be employee
class Customer(Person):
    def __init__(self,name,email,phonenumber,lastVisitedDate):
        super().__init__(name,email,phonenumber)
        self.lastVisitedDate=lastVisitedDate
    
    def __str__(self):
        return f"{super().__str__()}, last visited: {self.lastVisitedDate}"

#similarly an employee will inherit both from Person and will also be an abstractclass

class Employee(Person,ABC):
    def __init__(self,name,email,phonenumber,employeeId,joiningDate):
        super().__init__(name,email,phonenumber)
        self.employeeId=employeeId
        self.joiningDate=joiningDate
    
    def __str__(self):
        return f"{super().__str__()}, employee ID: {self.employeeId}, joined: {self.joiningDate}"

#here we will create separate classes called as Chef,Waiter,Receptionist,Manager
class Chef(Employee):
    def __init__(self,name,email,phonenumber,employeeId,joiningDate):
        super().__init__(name,email,phonenumber,employeeId,joiningDate)
    
    #create a helper function to prepare order
    def prepare_order(self):
        print(f"Chef {self.name} is preparing the order")

class Waiter(Employee):
    def __init__(self,name,email,phonenumber,employeeId,joiningDate):
        super().__init__(name,email,phonenumber,employeeId,joiningDate)
    
    def take_order(self):
        print(f"Waiter {self.name} is taking the order")

class Manager(Employee):
    def __init__(self,name,email,phonenumber,employeeId,joiningDate):
        super().__init__(name,email,phonenumber,employeeId,joiningDate)
    
    def add_employee(self):
        print(f"Manager {self.name} is adding a new employee")

class Receptionist(Employee):
    def __init__(self,name,email,phonenumber,employeeId,joiningDate):
        super().__init__(name,email,phonenumber,employeeId,joiningDate)
    
    def create_reservation(self):
        print(f"Receptionist {self.name} is creating a new reservation")

class EmployeeFactory:
    @staticmethod
    def create_factory(employeetype,name,email,phonenumber,employeeId,joiningDate):
        if(employeetype=="Chef"):
            return Chef(name,email,phonenumber,employeeId,joiningDate)
        elif(employeetype=="Waiter"):
            return Waiter(name,email,phonenumber,employeeId,joiningDate)
        elif(employeetype=="Manager"):
            return Manager(name,email,phonenumber,employeeId,joiningDate)
        else:
            raise ValueError(f"Unknown employee type:{employeetype}")
if __name__=="__main__":
    factory=EmployeeFactory()
    
    chef=factory.create_factory("Chef","harry","harry@gmail.com","3456789012","E001",datetime.now())
    chef.prepare_order()
    
    waiter=factory.create_factory("Waiter","ronnie","ronnie@gmail.com","456789032","D001",datetime.now())
    waiter.take_order()
    
    manager=factory.create_factory("Manager","hanna","hanna@gmail.com","890765432","B001",datetime.now())
    manager.add_employee()            
    
    
    
    
        
    
        