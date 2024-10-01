from abc import ABC,abstractmethod

#here customer,admin and ticketAgent
class Person(ABC):
    def __init__(self,name,address,email,phonenumber):
        self.name=name
        self.address=address
        self.email=email
        self.phonenumber=phonenumber
    
    @abstractmethod
    def get_details(self):
        pass

#here create classes for movie,booking and showtime
class Movie:
    def __init__(self,movieid,moviename):
        self.movieid=movieid
        self.moviename=moviename

class Booking:
    def __init__(self,bookingid,moviename,showtime):
        self.bookingid=bookingid
        self.moviename=moviename
        self.showtime=showtime
    
class Show:
    def __init__(self,showid,moviename,starttime):
        self.showid=showid
        self.moviename=moviename
        self.startime=starttime

#creating the customer class inheriting from the Person class
class Customer(Person):
    def __init__(self,name,address,email,phonenumber):
        #we will store the list of bookings
        self.bookings=[]
        super().__init__(name,address,email,phonenumber)
    
    def get_details(self):
        print(f"Customer has a name of {self.name} and has an email address of {self.email}")
    
    #now create three more methods to createbooking,updated booking and delete booking 
    def create_booking(self,booking):
        self.bookings.append(booking)
        print(f"Booking for {booking.bookingid} created for movie{booking.moviename}")
    
    def update_booking(self,booking,moviename):
        booking.moviename=moviename
        print(f"Booking for the following movie{booking.moviename} updated")
    
    def delete_booking(self,booking):
        self.bookings.remove(booking)
        print(f"Booking deleted successfully")

class Admin(Person):
    def __init__(self,name,address,email,phonenumber):
        self.shows=[]
        self.movies=[]
        super().__init__(name,address,email,phonenumber)
    
    def get_details(self):
        print(f"Admin has a name of {self.name} and has a phonenumber of {self.phonenumber}")
    
    #create helpers for addshow,deleteshow followed by add movie and delete movie
    def add_show(self,show):
        self.shows.append(show)
        print(f"Show has a showid {self.showid} and has a showtime of {self.showtime}")
    
    def delete_show(self,show):
        self.shows.remove(show)
        print(f"Show with {self.showid} has been deleted successfully")
    
#to be completed and factory design pattern needs to be added
    
    
        
        
        
    
    

        
        
    
        
    

    
        