import math
from collections import OrderedDict
from enum import Enum

from block_functions.attributes import Attribute

PointBuy = {
    7: -4,
    8: -2,
    9: -1,
    10: 0,
    11: 1,
    12: 2,
    13: 3,
    14: 5,
    15: 7,
    16: 10,
    17: 13,
    18: 17
}


class AbilityScore(Attribute):
    def __init__(self, name=None, base=10):
        super().__init__(name=name)
        self.base = base
        self.total = base
        self.modifier = math.floor((self.total - 10) / 2)
        self.point_buy = PointBuy[base]

    @staticmethod
    def add_bonus(self, args=None):
        if self.name:
            ...
        if args:
            for arg in args:
                print(arg)


class AbilityScores(Enum):
    STR = AbilityScore(name="Strength")
    DEX = AbilityScore(name="Dexterity")
    CON = AbilityScore(name="Constitution")
    INT = AbilityScore(name="Intelligence")
    WIS = AbilityScore(name="Wisdom")
    CHA = AbilityScore(name="Charisma")
    EMPTY = AbilityScore(name="EMPTY")

    @staticmethod
    def get_ability_scores():
        return OrderedDict([(score.name, score.value) for score in AbilityScores if score.name != "EMPTY"])
