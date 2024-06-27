from abc import ABC

class Person(ABC):
    def __init__(self,name,address,email,phone):
        self.name=name
        self.address=address
        self.email=email
        self.phone=phone
    
class Driver(Person):
    #here the driver will inherit from the Person
    def __init__(self,name,address,email,phone,driver_id):
        super().__init__(name,address,email,phone)
        self.driver_id=driver_id

