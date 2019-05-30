from player import Player
from room import Room

from item import Item
from item import LightSource

items = {
    "map": Item("map", "...this should help me in my journy."),
    "sword": Item("sword", "...a perfect item for slaying your enimies."),
    "shield": Item("shield", "...defend from your foes..."),
    "shiny pendant": Item("shiny pendant", "...the pendant contains a strange message in a language that you cant comprehend."),
    "lamp": LightSource("lamp", "...You better take this so that you can see in the caves!", True),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["sword"], items["shield"]], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["shiny pendant"], ], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [], False),

    'graveyard': Room("Grave Yard", """You find yourself in a large, damp, dark cavern.
In the center of the cavern, a light from the ceiling is lighting 3 matching 
grave stones.""", [items["lamp"]], True),
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

room['outside'].s_to = room['graveyard']
room['graveyard'].n_to = room['outside']


# create a new player
player_name = input("Please enter your name, adventurer!: ")

new_player = Player(player_name, room["outside"], [items["map"]])
print("(n, s, e, w) to move, 'take' or 'drop' to interact with items, 'i' or 'inventory' to see what youre holding...\n\n\n")


# handel player movement
def move_player(curRoom, direction):
    if direction == "n":
        if curRoom.n_to != None:
            new_player.current_room = curRoom.n_to
            if new_player.current_room.is_light == True:  # aware that this isnt the intended way of doing this... shoud use isinstance, but was having some issues getting that to do what i wanted, so keeping this for now
                print(f"{new_player.current_room.name}... ")
                print(f"{new_player.current_room.description}... ")
            else:
                if items["lamp"] in new_player.items:
                    print(f"{new_player.current_room.name}... ")
                    print(f"{new_player.current_room.description}... ")
                else:
                    print("Its pitch black in here! Turn back and find a light source!")
        else:
            print("You can not go that way, adventuruer!")
    elif direction == "s":
        if curRoom.s_to != None:
            new_player.current_room = curRoom.s_to
            if new_player.current_room.is_light == True:
                print(f"{new_player.current_room.name}... ")
                print(f"{new_player.current_room.description}... ")
            else:
                if items["lamp"] in new_player.items:
                    print(f"{new_player.current_room.name}... ")
                    print(f"{new_player.current_room.description}... ")
                else:
                    print("Its pitch black in here! Turn back and find a light source!")
        else:
            print("You can not go that way, adventuruer!")

    elif direction == "e":
        if curRoom.e_to != None:
            new_player.current_room = curRoom.e_to
            if new_player.current_room.is_light == True:
                print(f"{new_player.current_room.name}... ")
                print(f"{new_player.current_room.description}... ")
            else:
                if items["lamp"] in new_player.items:
                    print(f"{new_player.current_room.name}... ")
                    print(f"{new_player.current_room.description}... ")
                else:
                    print("Its pitch black in here! Turn back and find a light source!")
        else:
            print("You can not go that way, adventuruer!")

    else:
        if curRoom.w_to != None:
            new_player.current_room = curRoom.w_to
            if new_player.current_room.is_light == True:
                print(f"{new_player.current_room.name}... ")
                print(f"{new_player.current_room.description}... ")
            else:
                if items["lamp"] in new_player.items:
                    print(f"{new_player.current_room.name}... ")
                    print(f"{new_player.current_room.description}... ")
                else:
                    print("Its pitch black in here! Turn back and find a light source!")
        else:
            print("You can not go that way, adventuruer!")


# initial print of starting room
print(f"{new_player.current_room.name}... ")
print(f"{new_player.current_room.description}... ")


while True:

    if new_player.current_room.is_light == True:
        # print items in room
        if len(new_player.current_room.items) > 0:
            print("you see some items in this room")
            for i in new_player.current_room.items:
                print(f"    {i.name} {i.description}")
        else:
            print(f"There are no items to be seen in this room")

    # check for win state
    if new_player.current_room.name == "Treasure Chamber" and items["shiny pendant"] in new_player.current_room.items:
        print("The gods are pleased that you have returned the treasre.. Thank you for restoring the peace.")
        break

    # action input handlers
    action = input("\n\nWhat would you wish to do?:")
    # quit
    if action == "q":
        break
    # move
    elif action in ["n", "s", "e", "w"]:
        move_player(new_player.current_room, action)
    # take an item
    elif "take" in action:
        item = action[5:]
        if item in [item.name for item in new_player.current_room.items]:
            new_player.on_take(item)
            new_player.items.append(items[item])
            new_player.current_room.items.remove(items[item])
        else:
            print("that items dosnt exist here..")
    # drop an item
    elif "drop" in action:
        item = action[5:]
        if item in [item.name for item in new_player.items]:
            new_player.items.remove(items[item])
            new_player.current_room.items.append(items[item])
            if item == "lamp":
                print("It's not wise to drop your source of light!")
        else:
            print("You dont have that item to drop!")
    # show inventory
    elif action == "i":
        new_player.tell_items()
    elif action == "inventory":
        new_player.tell_items()
    # dont allow other input
    else:
        print("Sorry, but i cant read that input!")


print("See you soon, adventurer!")
