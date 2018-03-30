from enum import Enum

from .attributes import Attribute


class Save(Attribute):
    ...


class Saves(Enum):
    FORT = Save(name="Fortitude")
    REF = Save(name="Reflex")
    WILL = Save(name="Will")
    EMPTY = Save(name="EMPTY")
