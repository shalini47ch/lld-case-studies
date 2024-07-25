
class Invoice:
    def __init__(self,amount):
        self.amount=amount
        self.date=None
        self.customer=None
        self.items=[]
    #here we will create a dunder string method
    def __str__(self):
        return f"Invoice(amount={self.amount}, date={self.date}, customer={self.customer}, items={self.items})"
    
class InvoiceBuilder:
    def __init__(self,amount):
        self.invoice= Invoice(amount)
    
    def set_date(self,date):
        self.invoice.date=date
        return self
    
    def set_customer(self,customer):
        self.invoice.customer=customer
        return self
    
    def add_item(self,item):
        self.invoice.append(item)
        return 
    
    def build(self):
        return self.invoice
    
#here generating invoice is based on Invoice design pattern
        
        
    
        