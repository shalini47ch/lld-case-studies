from enums.PackageSize import PackageSize
from Location import Location
from Locker import Customer,Locker
from Strategylocation import EucledianDistance,ManhattenDistance
from AmazonLocker import AmazonLockerSystem

if __name__=="__main__":
    #here we will first create locker of various sizes
    locker1=Locker(1,PackageSize.SMALL)
    locker2=Locker(2,PackageSize.MEDIUM)
    locker3=Locker(3,PackageSize.LARGE)
    
    #now create a location for the locker
    location1=Location(37.7749, -122.4194,[locker1,locker2,locker3])
    customer1=Customer(12,37.7749,122.4194)
    
    #here create for eucledian strategy
    eucledian_strategy=EucledianDistance()
    amazon_locker=AmazonLockerSystem(eucledian_strategy)
    amazon_locker.add_location(location1)
    customer1.order_package(PackageSize.SMALL, amazon_locker)
    print(customer1.customerid)
    customer1.assignlocker(1234)
    # customer1.unassign_locker(123456) #this is for invalid pin
    # customer1.unassign_locker(customer1.pin)

    
    
    
    
    
    
    
    
    
    
     
    