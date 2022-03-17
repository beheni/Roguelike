"""
Module with game setting
"""


class Room:
    """
    Class for room
    """

    def __init__(self, name) -> None:
        """
        Initializes class object
        """
        self.name = name
        self.linked_rooms = {}
        self.item = None
        self.character = None
        self.description = None

    def set_description(self, description):
        """
        Sets the description of the room
        """
        self.description = description

    def link_room(self, room, side):
        """
        Links room to the particular side north, south, west or east
        """
        self.linked_rooms[side] = room

    def set_character(self, character):
        """
        Sets a character in the room
        """
        self.character = character

    def set_item(self, item):
        """
        Sets an item in the room
        """
        self.item = item

    def get_name(self):
        """
        Gets room's name
        """
        return self.name

    def get_details(self):
        """
        Print all the information about the room
        """
        print(self.name)
        print("-"*20)
        print(self.description)
        for side, room in self.linked_rooms.items():
            print(f"The {room.get_name()} is {side}")

    def get_character(self):
        """
        Gets room's character
        """
        return self.character

    def get_item(self):
        """
        Gets room's item
        """
        return self.item

    def move(self, side):
        """
        Moves from one room another linked to it
        """
        if side in self.linked_rooms:
            return self.linked_rooms[side]
        return "There is no room in that direction"


class Character:
    """
    Class for person
    """

    def __init__(self, name) -> None:
        """
        Initializes class object
        """
        self.name = name
        self.conversation = None

    def get_name(self):
        """
        Gets characters name
        """
        return self.name

    def set_conversation(self, conversation):
        """
        Sets conversation
        """
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f'[{self.get_name()} says]:{self.conversation}')
        else:
            print()


class Enemy(Character):
    """
    Class for enemies
    """
    defeated_enemies = 0

    def __init__(self, name, clas) -> None:
        """
        Initializes class object
        """
        super().__init__(name)
        self.clas = clas
        self.weakness = None

    def set_weakness(self, weakness):
        """
        Sets weakness for an enemy
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """
        Fights with an enemy
        """
        if fight_with == self.weakness:
            self.__class__.defeated_enemies += 1
            return True

    def get_defeated(self):
        """
        Counts defeated enemies
        """
        return self.__class__.defeated_enemies

    def describe(self):
        """
        Describes the enemy
        """
        print(f'{self.get_name()} is here!')
        print(self.clas)


class Friend(Character):
    """
    Class for friend
    """


class Item:
    """
    Class for items
    """

    def __init__(self, name) -> None:
        """
        Initializes class object
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        Sets the description of the room
        """
        self.description = description

    def get_name(self):
        """
        Gets item's name
        """
        return self.name

    def describe(self):
        """
        Describes the item
        """
        print(f"The {self.get_name()} is here - {self.description}")
