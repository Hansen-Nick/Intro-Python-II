from room import Room
from player import Player
import textwrap
from item import Item

# Declare all the rooms

items = {
    "sword": Item('sword', "Sharp object for poking and slicing stuff")
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['sword']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [])
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


new_player = Player(room['outside'], 'Nick')

while True:
    print(new_player.current_room.name)
    wrap_list = textwrap.wrap(
        new_player.current_room.description, width=50)
    for string in wrap_list:
        print(string)

    if len(new_player.current_room.items) == 0:
        print(f'This room does not contain any items')
    elif len(new_player.current_room.items) == 1:
        print(
            f'This room contains 1 item: a {new_player.current_room.items[0]}')

    user_input = input(
        'Which direction would you like to go? Enter q to quit:  ')

    if len(user_input.split()) == 1:
        if user_input == 'q':
            break
        elif user_input == 'n':
            try:
                new_player.current_room = new_player.current_room.n_to
            except:
                print("There is nothing in that direction")
        elif user_input == 'e':
            try:
                new_player.current_room = new_player.current_room.e_to

            except:
                print("There is nothing in that direction")

        elif user_input == 's':
            try:
                new_player.current_room = new_player.current_room.s_to

            except:
                print("There is nothing in that direction")
        elif user_input == 'w':
            try:
                new_player.current_room = new_player.current_room.w_to

            except:
                print("There is nothing in that direction")

    else:
        if user_input.split()[1] in items.keys():
            new_player.current_room.remove_item(items[user_input.split()[1]])
            new_player.add_to_inventory(items[user_input.split()[1]])
            print(items[user_input.split()[1]].on_take())
            print("room items", room['outside'].items)
            print("player inventory", new_player.inventory)

        # new_player.add_to_inventory(
        #     items[user_input.split()[1]]
        # )
        # print("new player items: ", new_player.inventory)
