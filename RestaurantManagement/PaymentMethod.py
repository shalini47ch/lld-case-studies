#here we will have different payment methods like cash,cheque,creditcard
from abc import ABC,abstractmethod
from enums.PaymentStatus import PaymentStatus
from datetime import datetime

class Payment(ABC):
    def __init__(self,paymentid,createdOn,amount,status):
        self.paymentid=paymentid
        self.createdOn=createdOn
        self.amount=amount
        self.status=status #this status we will obtain from the enum
        
    @abstractmethod
    def initiate_transaction(self):
        pass

class Cash(Payment):
    def __init__(self,paymentid,createdOn,amount,status,cashTendered):
        super().__init__(paymentid,createdOn,amount,status)
        self.cashTendered=cashTendered
    
    def initiate_transaction(self):
        #cash tendered is the amount you need to give to the cashier
        if(self.cashTendered>=self.amount):
            self.status=PaymentStatus.COMPLETED
            print(f"Transaction Completed: AMount to return {self.cashTendered-self.amount}")
        else:
            self.status=PaymentStatus.FAILED
            print(f"Transaction Failed")

#now similarly we will do for cheque and creditcard
#cheque will have bankName and the chequeNumber
class Cheque(Payment):
    def __init__(self,paymentid,createdOn,amount,status,bankName,chequeNumber):
        super().__init__(paymentid,createdOn,amount,status)
        self.bankName=bankName
        self.chequeNumber=chequeNumber
    
    #creating a helper function to initiate_transaction
    def initiate_transaction(self):
        print(f"Processing cheque payment with cheque number {self.chequeNumber} from bank {self.bankName}")

#similarly do it for CreditCard

class CreditCard(Payment):
    def __init__(self,paymentid,createdOn,amount,status,cardNumber,cardHolderName,expirydate,cvv):
        super().__init__(paymentid,createdOn,amount,status)
        self.cardNumber=cardNumber
        self.cardHolderName=cardHolderName
        self.expirydate=expirydate
        self.cvv=cvv
    
    def initiate_transaction(self):
        print(f"Processing credit card payment {self.cardHolderName} with card Number ending {self.cardNumber[-4:]}")

#now here we will create a factory and accordingly call the Cash,Cheque and CreditCard
class PaymentFactory:
    @staticmethod
    def createfactory(paymenttype,paymentid,createdOn,amount,status,**kwargs):
        if(paymenttype=="Cash"):
            return Cash(paymentid,createdOn,amount,status,kwargs.get("cashTendered"))
        elif(paymenttype=="Cheque"):
            return Cheque(paymentid,createdOn,amount,status,kwargs.get("bankName"),kwargs.get("chequeNumber"))
        elif(paymenttype=="CreditCard"):
            return CreditCard(paymentid,createdOn,amount,status,kwargs.get("cardNumber"),
                              kwargs.get("cardHolderName"),kwargs.get("expirydate"),kwargs.get("cvv"))
        else:
            raise TypeError("Invalid Payment Type:{paymenttype}")

if __name__=="__main__":
    factory=PaymentFactory()
    cashtrans=factory.createfactory("Cash",12,datetime.now(),230,PaymentStatus.COMPLETED,cashTendered=400)
    cashtrans.initiate_transaction()
    


    
        
        
        
    
    
    
    
    
    

