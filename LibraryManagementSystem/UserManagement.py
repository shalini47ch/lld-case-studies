from abc import ABC,abstractmethod
from enums.status import AccountStatus
from datetime import date

class User(ABC):
    def __init__(self,userid,name,email,status=AccountStatus.ACTIVE):
        self.userid=userid
        self.name=name
        self.email=email
    
    @abstractmethod
    def get_details(self):
        pass
#User is being implemented by the member and the librarian
#This entire user thing will follow the factory design pattern
class Member(User):
    def __init__(self,userid,name,email,date_of_membership,status=AccountStatus.ACTIVE):
        super().__init__(userid,name,email,status)
        self.date_of_membership=date_of_membership
        self.borrowed_books=[]
    
    def borrow_books(self,book_item):
        #here we will add the borrowed book to the list of borrowedbooks
        self.borrowed_books.append(book_item)
    
    def return_book(self,book_item):
        self.borrowed_books.remove(book_item)
    
    def get_details(self):
        return f"[Member id :{self.userid}, name:{self.name} {self.borrowed_books}]"
    
#now similarly do it for librarian
class Librarian(User):
    def __init__(self,userid,name,email,employee_id,status=AccountStatus.ACTIVE):
        super().__init__(userid,name,email)
        self.employee_id=employee_id
        
    def add_book(self,catalog,book_item):
        catalog.append(book_item)
    
    def remove_book(self,catalog,book_item):
        catalog.remove(book_item)
    
    def get_details(self):
        return f"[Librarian Id:{self.userid} name:{self.name} ]"
    
       
# obj=Member(12,"abc","abc2gmail.com",12)
# print(obj.get_details())

class UserFactory:
    #this will help us to create a user
    @staticmethod 
    def create_user(user_type,user_id,name,email,extra):
        if(user_type=="Member"):
            return Member(user_id,name,email,extra)
        elif(user_type=="Librarian"):
            return Librarian(user_id,name,email,extra)
        else:
            raise Exception("Invalid User Type")
#now here we are calling the client code
member=UserFactory.create_user("Member",12,"hanna","hanna@gmail.com",date.today())
member.borrow_books("abc")
print(member.get_details())

#So here in this part of our library management system we applied the factory design pattern

        
        