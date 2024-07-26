#here we will have a class called as meal which will have the list of meal items
from MealItem import MealItem

class Meal:
    def __init__(self,mealid):
        self.mealid=mealid
        self.mealItems=[]
    
    def add_MealItem(self,newItem):
        #here we will use isinstance to check if the newItem is an instance of the MealItem and if it is then push it in the list
        if(isinstance(newItem,MealItem)):
            self.mealItems.append(newItem)
        else:
            print(f"New item must be an instance of menu item")
    
    def __str__(self):
        meal_items_str = ', '.join([str(item) for item in self.mealItems])
        return f"Meal(mealid={self.mealid}, mealItems=[{meal_items_str}])"

meal = Meal(1)
print(meal)  # Output: Meal(mealid=1, mealItems=[])

item1 = MealItem(101, 2)
item2 = MealItem(102, 3)

meal.add_MealItem(item1)
meal.add_MealItem(item2)
print(meal)