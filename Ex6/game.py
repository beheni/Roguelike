"""
Module with game setting
"""


class Location:
    """
    Class for street
    """

    def __init__(self, name) -> None:
        """
        Initializes class object
        """
        self.name = name
        self.linked_locations = {}
        self.item = None
        self.character = None
        self.description = None

    def set_description(self, description):
        """
        Sets the description of the location
        """
        self.description = description

    def link_location(self, street, side):
        """
        Links street to the particular side north, south, west or east
        """
        self.linked_locations[side] = street

    def set_character(self, character):
        """
        Sets a character on the location
        """
        self.character = character

    def set_item(self, item):
        """
        Sets an item on the location
        """
        self.item = item

    def get_name(self):
        """
        Gets streets's name
        """
        return self.name

    def get_details(self):
        """
        Print all the information about the location
        """
        print(self.name)
        print("-"*20)
        print(self.description)
        for side, street in self.linked_locations.items():
            print(f"{street.get_name()} за напрямком {side}")

    def get_character(self):
        """
        Gets street's character
        """
        return self.character

    def get_item(self):
        """
        Gets street 's item
        """
        return self.item

    def move(self, side):
        """
        Moves from one street to another linked to it
        """
        if side in self.linked_locations:
            return self.linked_locations[side]
        return "Нема куда туди йти("


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
        """
        Prints character's words
        """
        if self.conversation is not None:
            print(f'[{self.get_name()} каже]: {self.conversation}')
        else:
            print()


class Enemy(Character):
    """
    Class for enemies
    """

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
            return True

    def describe(self):
        """
        Describes the enemy
        """
        print(f'{self.get_name()} тут!')
        print(self.clas)


class Friend(Character):
    """
    Class for friend
    Inherits from Character class therefore can be used for furute fun
    """

    def __init__(self, name, description) -> None:
        super().__init__(name)
        self.description = description
        self.conversation = "Go and beat its ass"

    def describe(self):
        """
        Describes the friend
        """
        print(f'{self.get_name()} є тут!')
        print(self.description)


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
        Sets the description of the item
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
        print(f"Тут є {self.get_name()} - {self.description}")
