from abc import ABC,abstractmethod
from enums.VehicleStatus import VehicleStatus

class Vehicle(ABC):
    def __init__(self, vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage):
        self.vehicle_id=vehicle_id
        self.license_number=license_number
        self.passenger_capacity=passenger_capacity
        self.has_sunroof=has_sunroof
        self.status=VehicleStatus.AVAILABLE
        self.model=model
        self.manufacturing_year=manufacturing_year
        self.mileage=mileage
        self.log=[]
    
    def reserve_vehicle(Vehicle):
        if(self.status=="AVAILABLE"):
            self.status="RESERVED"
            self.log.append("Vehicle Reserved")
            return True #this means we were able to reserve the vehicle
        return False
    
    def return_vehicle(Vehicle):
        if(self.status=="RESERVED"):
            self.status="AVAILABLE"
            self.log.append("Vehicle Returned")
            return True
        return False
    
    
    def get_log(self):
        return self.log
    
class Car(Vehicle):
    def __init__(self,vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage,car_type):
        super().__init__(vehicle_id,license_number,passenger_capacity,has_sunroof,status,model,manufacturing_year,mileage)
        self.car_type=car_type
    
    def getcar_type(self):
        return self.car_type

#similarly do it for motorcycle and van and truck
class Motorcycle(Vehicle):
    def __init__(self,vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage,motorcycle_type):
        super().__init__(vehicle_id,license_number,passenger_capacity,has_sunroof,status,model,manufacturing_year,mileage)
        self.motorcycle_type=motorcycle_type
        
    def get_motorcycle_type(self):
        return self.motorcycle_type

#similarly do it for van and truck
class Van(Vehicle):
    def __init__(self,vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage,van_type):
        super().__init__(vehicle_id,license_number,passenger_capacity,has_sunroof,status,model,manufacturing_year,mileage)
        self.van_type=van_type
    
    def get_van_type(self):
        return self.van_type

#similarly do it for truck
class Truck(Vehicle):
    def __init__(self,vehicle_id, license_number, passenger_capacity, has_sunroof, status, model, manufacturing_year, mileage,truck_type):
        super().__init__(vehicle_id,license_number,passenger_capacity,has_sunroof,status,model,manufacturing_year,mileage)
        self.truck_type=truck_type
    
    def get_truck_type(self):
        return self.truck_type


    

    
         
         
         
    


    
            