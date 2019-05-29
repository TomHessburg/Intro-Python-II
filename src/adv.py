from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

from player import Player

player_name = input("Please enter your name, adventurer!: ")

new_player = Player(player_name, room["outside"])





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

    elif direction == "w":
        if curRoom.w_to != None:
            new_player.current_room = curRoom.w_to
            
        else:
            print("\nYou can not go that way, adventuruer!")
    else:
        print("\nSorry, that is not a direction.... what are they teaching these kids nowasays...")
    



while True:
    print(f"\n{new_player.name} finds him/herself {new_player.current_room.name}")
    print(f"{new_player.current_room.description}")

    direction = input("\nwhich direction do you wish to travel from here? (n, s, e, w):")
    if direction == "q":
        break
    move_player(new_player.current_room, direction)


print("See you soon, adventurer!")