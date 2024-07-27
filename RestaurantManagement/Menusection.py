#here we will create a menusection and use the menuitem in it
from MenuItem import MenuItem
class MenuSection:
    def __init__(self, title):
        self.title = title
        self.items = []

    def add_item(self, item_name, item_price):
        self.items.append({"name": item_name, "price": item_price})

    def getMenuItems(self):
        return self.items


    
    