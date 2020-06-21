# Write a class to hold player information, e.g. what room they are in
# currently.
from colors import prRed, prGreen, prYellow, prCyan, prLightGray, prPurple
from lightsource import LightSource
class Player():
    directions = {
        "n": "North",        
        "s":  "South",
        "e": "East",
        "w":  "West"
    }

    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.is_light = False

    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room:
            self.current_room = next_room
        else:
            prRed(f"There is no room to the {self.directions[direction]} of this room\n")

    def grabItem(self, item):
        print(f"current room light: {self.current_room.is_light}")
        print(f"player Light: {self.is_light}")
        if not self.is_light and not self.current_room.is_light:
            prYellow(f"Good luck finding {item.name} in the dark\n")
        elif item in self.inventory:
            prYellow(f"You already have {item.name} in your inventory\n")
        else:
            self.inventory.append(item)
            self.current_room.removeItem(item)
            prGreen(f"You have picked up {item.name}\n")
            if isinstance(item, LightSource):
                self.is_light = True

    def dropItem(self, itemName):
        for item in self.inventory:
            if itemName == item.name and isinstance(item, LightSource):
                self.inventory.remove(item)
                self.current_room.addItem(item)
                item.onDrop()
                self.is_light = False
                prYellow(f"You have dropped {item.name} from your inventory\n")
                return
            elif itemName == item.name:
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