from room import Room

from item import Item

items = {
    "map": Item("map... ", "this should help me in my journy."),
    "sword": Item("sword... ", "A perfect item for slaying your enimies."),
    "shield": Item("shield... ", " Defend from your foes..."),
    "shiny-pendant": Item("shiny-pendant... ", "the pendant contains a strange message in a language that you cant comprehend."),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["sword"], items["shield"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["shiny-pendant"],]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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


#make player
from player import Player

player_name = input("Please enter your name, adventurer!: ")

new_player = Player(player_name, room["outside"], [items["map"]])
print("(n, s, e, w) to move, 'take' or 'drop' to interact with items, 'i' or 'inventory' to see what youre holding...")




def move_player(curRoom, direction):
    if direction == "n":
        if curRoom.n_to != None:
            new_player.current_room = curRoom.n_to
            
        else:
            print("\nYou can not go that way, adventuruer!")
    elif direction == "s":
        if curRoom.s_to != None:
            new_player.current_room = curRoom.s_to
            
        else:
            print("\nYou can not go that way, adventuruer!")

    elif direction == "e":
        if curRoom.e_to != None:
            new_player.current_room = curRoom.e_to
            
        else:
            print("\nYou can not go that way, adventuruer!")

    else:
        if curRoom.w_to != None:
            new_player.current_room = curRoom.w_to
            
        else:
            print("\nYou can not go that way, adventuruer!")
    


while True:
    
    print(f"\n{new_player.current_room.name}... ")
    print(f"{new_player.current_room.description}... \n")
    
    ##print items in room
    if len(new_player.current_room.items) > 0:
        print("you see some items in this room\n")
        for i in new_player.current_room.items:
            print(f"    {i.name} {i.description}")
    else:
        print(f"There are no items to be seen in this room")

    
    
    #check for win state
    if new_player.current_room.name == "Treasure Chamber" and items["shiny-pendant"] in new_player.current_room.items:
        print("\n\n\nThe gods are pleased that you have returned the treasre.. Thank you for restoring the peace.")
        break



    #action input handlers
    action = input("\n\n\n\n\nWhat would you wish to do?:")
    #quit
    if action == "q":
        break
    #move
    elif action == "n" or action == "s" or action == "e" or action == "w":
        move_player(new_player.current_room, action)
    #take an item
    elif "take" in action:
        item = action[5:]
        if items[item] in new_player.current_room.items:
            new_player.on_take(item)
            new_player.items.append(items[item])
            new_player.current_room.items.remove(items[item])
        else:
            print("that items dosnt exist here..")
    #drop an item
    elif "drop" in action:
        item = action[5:]
        if items[item] in new_player.items:  
            new_player.items.remove(items[item])
            new_player.current_room.items.append(items[item])
        else:
            print("You dont have that item to drop!")
    #show inventory
    elif action == "i":
        new_player.tell_items()
    elif action == "inventory":
        new_player.tell_items()
    #dont allow other input
    else:
        print("\nSorry, but i cant read that input!")


print("See you soon, adventurer!")