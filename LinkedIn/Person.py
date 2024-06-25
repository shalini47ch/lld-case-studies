#here we create an abstract class called as Person and the admin and User will inherit from it
from abc import ABC,abstractmethod
from Address import Address

class Person(ABC):
    def __init__(self,name,address,email,phonenumber):
        self.name=name
        self.address=Address #this will have the address from the address file
        self.email=email
        self.phonenumber=phonenumber
        
    
    #implement the getter and setter
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_email(self):
        return self.email
    
    def get_phonenumber(self):
        return self.phonenumber
    
    def get_account(self):
        return self.account

class Admin(Person):
    def __init__(self,name,address,email,phonenumber):
        super().__init__(name,address,email,phonenumber)
    
    def execute(self,command):
        command.execute()

#similarly create a user 
class User(Person):
    def __init__(self,name,address,email,phonenumber):
        super().__init__(name,address,email,phonenumber)
    
    def view_profile(self):
        print(f"Viewing of profile {self.name}")

#here there will be two classes called as Admin and User who will inherit from the abstract class called as person
#the users we will use here will follow the command design pattern

#now here we will apply the command design pattern
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
#here we will implement the BlockUserCommand ,UnblockUserCommand,DisablePage,EnablePage,DeleteGroupCommand

class BlockUserCommand(Command):
    def __init__(self,admin,user):
        self.admin=admin
        self.user=user
    
    def execute(self):
        print(f"{self.admin.name} is blocking {self.user.name}")

class UnblockUserCommand(Command):
    def __init__(self,admin,user):
        self.admin=admin
        self.user=user
    
    def execute(self):
        print(f"{self.admin.name} is unblocking {self.user.name}")

#create a helper function to disablePage Command
class DisablePageCommand(Command):
    def __init__(self,admin,page):
        self.admin=admin
        self.page=page
    
    def execute(self):
        print(f"{self.admin.name} is disabling page {self.page.name}")

class EnablePageCommand(Command):
    def __init__(self,admin,page):
        self.admin=admin
        self.page=page
    
    def execute(self):
        print(f"{self.admin.name} is enabling page {self.page.name}")

class DeleteGroupCommand(Command):
    def __init__(self,admin,group):
        self.admin=admin
        self.group=group
    
    def execute(self):
        print(f"{self.admin.name} is deleting group {self.group.name}")

class Page:
    def __init__(self,name):
        self.name=name

#similarly do it for group
class Group:
    def __init__(self,name):
        self.name=name

admin=Admin("admin1","bangalore","admin1@gmail.com","6789054323")
user=User("user1","mumbai","user1@gmail.com","897654323")
page=Page("Page1")
group=Group("group1")

blockuser=BlockUserCommand(admin,user)
unblockuser=UnblockUserCommand(admin,user)
disablepage=DisablePageCommand(admin,user)
enablepage=EnablePageCommand(admin,user)
deletegroup=DeleteGroupCommand(admin,user)

admin.execute(blockuser)
admin.execute(unblockuser)
admin.execute(disablepage)
admin.execute(enablepage)
admin.execute(deletegroup)

#so here the command design pattern is added



        
        
    
    
    
    
    




    
        