from item import Item
from colors import prYellow

class LightSource(Item):
    def __init__(self,name,description):
        super().__init__(name, description)

    def onDrop(self):
        prYellow("It's not wise to drop your source of light!")
