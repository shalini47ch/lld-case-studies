#here we will have a class to keep track of the meal item with a specific mealid and the quantity of the meal item
class MealItem:
    def __init__(self,meal_id,quantity):
        self.meal_id=meal_id
        self.quantity=quantity
    
    def updateQuantity(self,newQuantity):
        if(newQuantity>=0):
            self.quantity=newQuantity
        else:
            print("The value of the quantity cannot be negative")
    
    #here we will create a dunder string method to print 
    def __str__(self):
        return f"MealItem has a mealid:{self.meal_id} and a quantity of {self.quantity}"

meal=MealItem(123,10)
meal.updateQuantity(12)
print(meal)

#similarly try it for negative sides
meal.updateQuantity(-10)
print(meal)



        
