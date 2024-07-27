class MenuItem:
    #it will have parameters like id,title,description and price
    def __init__(self,menuid,title,description,price):
        self.menuid=menuid
        self.title=title
        self.description=description
        self.price=price
    
    def updatePrice(self, new_price):
        if isinstance(new_price, (int, float)) and new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Price must be a non-negative number")

    def updateDetails(self, title=None, description=None):
        if title:
            self.title = title
        if description:
            self.description = description

        