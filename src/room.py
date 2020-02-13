# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    n_to = None
    s_to = None
    e_to = None
    w_to = None
    

    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"This room is {self.name}"

    def hasItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                return True
        
        return False

# Delete addItem and removeItem methods
    def addItem(self, item):
        self.items.append(item)
        print(f"items print from addItem: {self.items}")
    
    def removeItem(self, item):
        self.items.remove(item)