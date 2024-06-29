from abc import ABC,abstractmethod

#here we need to search the vehicle on the basis of parameters like type,model and using the strategy design pattern for it

class SearchStrategy(ABC):
    @abstractmethod
    def search(self,vehicles,query):
        pass

class SearchByType(SearchStrategy):
    def search(self,vehicles,vehicle_type):
        return [vehicle for vehicle in vehicles if vehicle["type"]==vehicle_type]

#similarly create another class for SearchByModel

class SearchByModel(SearchStrategy):
    def search(self,vehicles,model):
        return [vehicle for vehicle in vehicles if vehicle["model"]==model]

#now here creating the context
class VehicleCatalog:
    def __init__(self):
        self.vehicles=[]
        self.search_strategy=None
    
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)
    
    def set_searchstrategy(self,strategy):
        self.search_strategy=strategy
    
    def search(self, query):
        if not self.search_strategy:
            raise ValueError("Search strategy not set")
        return self.search_strategy.search(self.vehicles, query)

if __name__=='__main__':
    catalog=VehicleCatalog()
    catalog.add_vehicle({"type":"SUV","model":"Model A","make":"Hyundai"})
    #similarly add other vehicles
    catalog.add_vehicle({"type":"Sedan","model":"Model S","make":"Tesla"})
    catalog.add_vehicle({"type":"Nano","model":"Model N","make":"Tata"})
    catalog.set_searchstrategy(SearchByType())
    suv_vehicles=catalog.search("SUV")
    print("SUV",suv_vehicles)
    print("****************************")
    catalog.set_searchstrategy(SearchByModel())
    suv_vehicles=catalog.search("Model S")
    print("Sedan",suv_vehicles)
    
    
    
    

           
    