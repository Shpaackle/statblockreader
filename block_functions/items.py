from enum import Enum


class Item:
    def __init__(self, name):
        self.name = name


class Items(Enum):
    Rapier = Item(name="Rapier")
    EMPTY = Item(name="EMPTY")
