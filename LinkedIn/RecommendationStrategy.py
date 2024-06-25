from abc import ABC,abstractmethod 
from FeedUpdates import User

class RecommendationStrategy(ABC):
    @abstractmethod
    def recommend(self,user):
        pass

class ContentRecommendationStrategy(RecommendationStrategy):
    def recommend(self,user):
        #here recommend user on the basis of logic
        return ["Post1","Post2"]

class ConnectionRecommendationStrategy(RecommendationStrategy):
    def recommend(self,user):
        return ["User1","User2"]

#now here declaring the main function
class RecommendationEngine:
    def __init__(self,strategy):
        self.strategy=strategy
    
    def recommend(self,user):
        return self.strategy.recommend(user)
user = User("John Doe")
content_strategy = ContentRecommendationStrategy()
engine = RecommendationEngine(content_strategy)
recommendations = engine.recommend(user)
print(recommendations) 


    