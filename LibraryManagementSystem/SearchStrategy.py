#Here we need to perform search by title,author,publisherdate,subject
from abc import ABC,abstractmethod 
from Book import Book
from enums.format import BookFormat

class SearchStrategy(ABC):
    @abstractmethod
    def search(self,catalog,query):
        pass

class TitleSearchStrategy(SearchStrategy):
    def search(self,catalog,query):
        return [book for book in catalog.books if query.lower() in book.title.lower()]

#similarly create it for searchbyauthor
class AuthorSearchStrategy(SearchStrategy):
    def search(self,catalog,query):
        return [book for book in catalog.books if query.lower() in book.author.lower()]
    
#create a helper functuon to searchbysubject
class SubjectSearchStrategy(SearchStrategy):
    def search(self,catalog,query):
        return [book for book in catalog.books if query.lower() in book.subject.lower()]

#here create a helper function called as catalog
class Catalog:
    def __init__(self):
        self.books=[]
        self.search_strategy=None
    
    def add_book(self,book):
        self.books.append(book)
        
    def set_search_strategy(self,strategy):
        self.search_strategy=strategy
    
    def search(self,query):
        if self.search_strategy:
            return self.search_strategy.search(self, query)
        else:
            raise ValueError("Search strategy not set")

catalog=Catalog()
catalog.add_book(Book(12,"HarryPotter","xyz","pqr",BookFormat.PAPERBACK,"Jk rowling"))

titlesearch=catalog.set_search_strategy(TitleSearchStrategy())

booksfound=catalog.search("HarryPotter")
for book in booksfound:
    print(f"Found book: {book.title} by {book.author}")
    


        
