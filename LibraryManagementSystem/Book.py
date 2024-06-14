from abc import ABC,abstractmethod

class Book(ABC):
    def __init__(self,isbn,title,subject,publisher,bookformat,author):
        self.isbn=isbn
        self.title=title
        self.subject=subject
        self.publisher=publisher
        self.bookformat=bookformat
        self.author=author
    
    #create a helper function to return the getdetails
    def get_details(self):
        pass
    
    
        