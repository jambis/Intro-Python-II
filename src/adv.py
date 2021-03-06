from room import Room
from player import Player
from item import Item
from lightsource import LightSource
from colors import prRed, prGreen, prYellow, prCyan, prLightGray, prPurple
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}

# Declare items

items = {
    'sword':    Item("sword", "It's dangerous to go alone, take this dull blade!"),
    "shield":   Item("shield", "A basic shield"),
    "wand":     Item("wand", "Not quite the a deahtly hallow but it will do"),
    "lamp":     LightSource("lamp", "You should take this so you can see inside the cave")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room['foyer'].items = [items['shield']]
room['outside'].items = [items['sword'], items['lamp']]
room['treasure'].items = [items['wand']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(isinstance(items['lamp'], LightSource))

userName = input("What is your name? ")
player = Player(userName,room["outside"])
prCyan(f"Welcome to the game {player.name}\n")
prCyan("--------------------------------------------------\n")

while True:
    if player.is_light or player.current_room.is_light:
        print(f"You are in: {player.current_room.name}")
        print(f"{player.current_room.description}\n")
        player.printRoomItems()
    else:
        print(f"The room is pitch black")
        
    userMove = input(f"""\033[93m
Enter a cardinal direction (n, s, w, e) to move in that direction.
You can check your inventory by typing 'i' or 'inventory' 
You can also pick up items by typing 'get <item_name>'
You can drop items by typing 'drop <item_name>'
Enter q to quit the game.\033[00m
""").lower()
  
    if userMove in ["n", "s", "e", "w"]: 
        player.move(userMove)
    elif userMove.startswith("get"):
        words = userMove.split()
        if len(player.current_room.items) > 0 and player.current_room.hasItem(words[1]):
            player.grabItem(items[words[1]])
        else:
            prRed(f"This room doesn't have a {words[1]}")
    elif userMove.startswith("drop"):
        words =  userMove.split()
        player.dropItem(words[1])
    elif userMove == "i" or userMove == "inventory":
        player.printInventory()
    elif userMove == "q":
        exit()
    else:
        prRed("Invalid input, try again!\n")
    

