#Here we can perform payments through various types of transactions like creditCard,CashTransaction,CheckTransaction

from abc import ABC,abstractmethod 
from enums.AccountStatus import AccountStatus
from datetime import datetime

class BillTransaction(ABC):
    def __init__(self,creationDate,amount,status):
        self.creationDate=creationDate
        self.amount=amount
        self.status=status

    @abstractmethod
    def initiate_transaction(self):
        pass

#here we will have different types of transactions like check transactions,creditcard transactions and cash transactions
class ChequeTransaction(BillTransaction):
    def __init__(self,creationDate,amount,status,bankName,checkNumber):
        super().__init__(creationDate,amount,AccountStatus.ACTIVE)
        self.bankName=bankName
        self.checkNumber=checkNumber
    
    def initiate_transaction(self):
        print(f"Processing cheque transaction:Bank-{self.bankName},Cheque Number:{self.checkNumber}")
        
#now the next one is the creditCard Transaction
class CreditCardTransaction(BillTransaction):
    def __init__(self,creationDate,amount,status,creditCardName,zipcode):
        super().__init__(creationDate,amount,AccountStatus.ACTIVE)
        #here the zipcode indicates the city where it was issuedAt
        self.creditCardName=creditCardName
        self.zipcode=zipcode
    
    def initiate_transaction(self):
        print(f"Processing credit card payment:CreditCardName:{self.creditCardName},Zipcode:{self.zipcode}")
        
        

class CashTransaction(BillTransaction):
    def __init__(self,creationDate,amount,status,cashTendered):
        super().__init__(creationDate,amount,AccountStatus.ACTIVE)
        self.cashTendered=cashTendered
    
    def initiate_transaction(self):
        #here creating the initiate_transaction method
        print(f"Processing cash transaction:cash Tendered:{self.cashTendered}")
        
        
        
#we can use the factory design pattern to solve this
class TransactionFactory:
    @staticmethod
    def create_transaction(transaction_type,creationDate,amount,**kwargs):
        #kwargs to take additional parameters in account
        if(transaction_type=="Cheque"):
            return ChequeTransaction(creationDate,amount,AccountStatus.ACTIVE,kwargs.get("bankName"),kwargs.get("checkNumber"))
        elif(transaction_type=="CreditCard"):
            return CreditCardTransaction(creationDate,amount,AccountStatus.ACTIVE,kwargs.get("creditCardName"),kwargs.get("zipcode"))
        elif(transaction_type=="Cash"):
            return CashTransaction(creationDate,amount,AccountStatus.ACTIVE,kwargs.get("cashTendered"))
        else:
            raise ValueError("Unknown transaction type:{transaction_type}")
if __name__=="__main__":
    factory=TransactionFactory()
    chequetrans=factory.create_transaction("Cheque",datetime.now(),120,bankName="SBI",checkNumber=4567980)
    chequetrans.initiate_transaction()
    
    
    

    
    
        
    

    
    
        
    

        

