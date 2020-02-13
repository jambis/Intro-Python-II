# Implement a class to hold room information. This should have name and
# description attributes.
class Room():

    

    def __init__(self, name, description, is_light, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_light = is_light
        

    def __str__(self):
        return f"This room is {self.name}"

    def hasItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                return True
        
        return False

    def addItem(self, item):
        self.items.append(item)
    
    def removeItem(self, item):
        self.items.remove(item)