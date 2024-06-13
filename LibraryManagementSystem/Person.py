from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,address,email,phone):
        self.name=name
        self.address=address
        self.email=email
        self.phone=phone

    