from Menusection import MenuSection

class Menu:
    def __init__(self, menuid, title, description, price,menusections):
        self.menuid = menuid
        self.title = title
        self.description = description
        self.price = price
        self.menusections = menusections if menusections else []

    def addMenuSection(self, menusection):
        if isinstance(menusection, MenuSection):
            self.menusections.append(menusection)
        else:
            raise TypeError("Only MenuSection objects can be added to the menu")

    def removeMenuSection(self, menusection):
        if menusection in self.menusections:
            self.menusections.remove(menusection)
        else:
            print("MenuSection not found in this menu")

    def getMenuSections(self):
        return self.menusections

    def updateMenuDetails(self, title=None, description=None, price=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if price is not None:
            if isinstance(price, (int, float)) and price >= 0:
                self.price = price
            else:
                raise ValueError("Price must be a non-negative number")

    def getMenuSection(self, section_title):
        for section in self.menusections:
            if section.title == section_title:
                return section
        return None

    def getTotalMenuItems(self):
        return sum(len(section.getMenuItems()) for section in self.menusections)