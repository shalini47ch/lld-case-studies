#Here there are three types of payments creditCard,Cash and UPI
from abc import ABC,abstractmethod 
from enums.PaymentStatus import PaymentStatus
from Address import Address

class Payment(ABC):
    def __init__(self,amount,status):
        self.amount=amount
        self.status=status
    
    @abstractmethod
    def make_payment(self):
        pass

class CreditCard(Payment):
    def __init__(self,amount,status,nameOnCard,cardNumber):
        super().__init__(amount,status)
        self.nameOnCard=nameOnCard
        self.cardNumber=cardNumber
        # self.billingAddress=billingAddress
        # self.expiryDate=expiryDate
    
    def make_payment(self):
        print(f"Payment made by credit card by cardNumber {self.cardNumber}")


class Cash(Payment):
    def __init__(self,amount,status,billingAddress):
        super().__init__(amount,status)
        self.billingAddress=billingAddress
    
    def make_payment(self):
        print(f"Payment made by cash in the billing_address {self.billingAddress}")
    
class UPI(Payment):
    def __init__(self,amount,status,upiid,paidat):
        super().__init__(amount,status)
        self.upiid=upiid
        self.paidat=paidat
    
    def make_payment(self):
        print(f"Payment made by upi by the upiid of {self.upiid}")

#now here create a payment factory and call on the basis of payment
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type,amount,status,**kwargs):
        if(payment_type=="CreditCard"):
            return CreditCard(amount,status,kwargs.get("nameOnCard"),kwargs.get("cardNumber"))
        elif(payment_type=="Cash"):
            return Cash(amount,status,kwargs.get("billingAddress"))
        elif(payment_type=="UPI"):
            return UPI(amount,status,kwargs.get("upiid"),kwargs.get("paidat"))
        else:
            raise ValueError("Unknown payment type")

if __name__=="__main__":
    
    creditcardpayment=PaymentFactory.create_payment("CreditCard",12,PaymentStatus.CONFIRMED,nameOnCard="hanna",cardNumber=5467890321)
    creditcardpayment.make_payment()
    
    #similarly do it for cash and then UPI
    add=Address(5679,"bangalore","bangalore","India","Karnataka")
    cashpayment=PaymentFactory.create_payment("Cash",120,PaymentStatus.CONFIRMED,billingAddress=add)
    cashpayment.make_payment()
    
    
    
    
    
        
    
    


        
        
    
        
        
        
        

