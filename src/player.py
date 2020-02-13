# Write a class to hold player information, e.g. what room they are in
# currently.
from colors import prRed, prGreen, prYellow, prCyan, prLightGray, prPurple
class Player():
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def grabItem(self, item):
        if item in self.inventory:
            prYellow(f"You already have {item.name} in your inventory\n")
        else:
            self.inventory.append(item)
            self.current_room.removeItem(item)
            prGreen(f"You have picked up {item.name}\n")

    def dropItem(self, itemName):
        for item in self.inventory:
            if itemName == item.name:
                self.inventory.remove(item)
                self.current_room.addItem(item)
                prYellow(f"You have dropped {item.name} from your inventory\n")
                return
            
        prRed(f"You don't have {itemName} in your inventory, therefore you can't drop it\n")

    def printRoomItems(self):
        if len(self.current_room.items) > 0:
            for item in self.current_room.items:
                prPurple(f"This room contains: {item.name}")
        else:
            return
    
    def printInventory(self):
        if len(self.inventory) > 1:
            allItems = "Your inventory: "
            for item in self.inventory:
                allItems += item.name + ", "
            prPurple(f"{allItems[:-2]}\n")
        elif len(self.inventory) > 0:
            prPurple(f"Your inventory: {self.inventory[0].name}\n")
        else:
            prPurple("Your inventory is empty\n")