
from enums.AccountStatus import AccountStatus
from Address import Address

class Account:
    def __init__(self,userName,password,name,email,phone,status,shippingAddress):
        self.userName=userName
        self.password=password
        self.name=name
        self.email=email
        self.phone=phone
        self.status=status
        self.shippingAddress=shippingAddress
        self.products=[] #this will store the list of products
        self.productReview=[] #this will store the list of productReview
        
    #here we need to add getter and setters and then create functions like addProduct,addProductReview,deleteProduct,deleteProductView,resetPassword
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
    
    def addProduct(self):
        self.products.append("Tv")
        self.products.append("Washing Machine")
        self.products.append("Fridge")
     
    def addProductReview(self):
        self.productReview.append("The tv has a rating of 5 star")
        self.productReview.append("The installation was not up to the mark")
    
    def getListOfProducts(self):
        return self.products
    
    def getListOfReviews(self):
        return self.productReview

account=Account("ronita2345","abc@1234","ronita","ronita@gmail.com",89456789021,AccountStatus.ACTIVE,Address)
account.addProduct()
print(account.getListOfProducts())



    
    
        