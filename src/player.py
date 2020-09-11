# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, name):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def __str__(self):
        return f"The player named {self.name} is currently in room {self.current_room}"
