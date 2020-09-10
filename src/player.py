# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, name):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"The player named {self.name} is currently in room {self.current_room}"
