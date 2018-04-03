from enum import Enum

from .attributes import Attribute


class Save(Attribute):
    def __init__(self, name):
        super(Save, self).__init__(name=name)


class Saves(Enum):
    FORT = Save(name="Fortitude")
    REF = Save(name="Reflex")
    WILL = Save(name="Will")
    EMPTY = Save(name="EMPTY")
