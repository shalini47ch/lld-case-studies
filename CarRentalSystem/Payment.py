from abc import ABC,abstractmethod
from enums.PaymentStatus import PaymentStatus
from datetime import datetime

class Payment(ABC):
    def __init__(self,amount,timestamp,status):
        self.amount=amount
        self.timestamp=timestamp
        self.status=PaymentStatus.UNPAID
    
    @abstractmethod
    def make_payment(self):
        pass

#two payment methods one is credit card other is cash
class Cash(Payment):
    def __init__(self,amount,timestamp,status):
        super().__init__(amount,timestamp,status)
    
    def make_payment(self):
        self.status=PaymentStatus.PAID
        print("Cash payment completed")
    
    def get_amount(self):
        return self.amount
    
    def get_timestamp(self):
        return self.timestamp

class CreditCard(Payment):
    def __init__(self,amount,timestamp,status,name_on_card, card_number, billing_address, code):
        super().__init__(amount,timestamp,status)
        self.name_on_card=name_on_card
        self.card_number=card_number
        self.billing_address=billing_address
        self.code=code
    
    def make_payment(self):
        self.status=PaymentStatus.PAID
        print("Credit Card Payment Completed")
    
    def get_amount(self):
        print(self.amount)
    
    def get_timestamp(self):
        print(self.timestamp)

#now here we will apply the factory design pattern to choose the payment_type
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type,amount,timestamp,status,**kwargs):
        if(payment_type=="Cash"):
            return Cash(amount,timestamp,status)
        elif(payment_type=="CreditCard"):
            return CreditCard(amount,timestamp,status,kwargs.get("name_on_card"),kwargs.get("card_number"),
                              kwargs.get("billing_address"),kwargs.get("code"))
        else:
            raise ValueError("Unknown payment type")

if __name__=="__main__":
    timestamp=datetime.now()
    cash_payment=PaymentFactory.create_payment("Cash","1200",timestamp,PaymentStatus.PENDING)
    cash_payment.make_payment()
    print(cash_payment.get_amount())
    print(cash_payment.get_timestamp())
    
    
    

            
        

    
    
    
    
        


