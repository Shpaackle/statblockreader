import math
from collections import OrderedDict
from enum import Enum

from block_functions.attributes import Attribute

# Dictionary to hold point buy values
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


# subclass of Attribute
# Used primarily for ability scores
class AbilityScore(Attribute):
    def __init__(self, name=None, base=10):
        super().__init__(name=name)
        self.base = base
        self.total = base
        self.modifier = self._modifier()
        self.point_buy = PointBuy[base]

    def _modifier(self):
        return math.floor((self.total - 10) / 2)

    @staticmethod
    def add_bonus(self, args=None):
        if self.name:
            ...
        if args:
            for arg in args:
                print(arg)


# enum to hold ability scores
class AbilityScores(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"
    EMPTY = "EMPTY"

    # creates ability scores for object
    @staticmethod
    def get_ability_scores():
        score_dict = OrderedDict()
        for score in AbilityScores:
            if score.name != "EMPTY":
                score_dict[score] = AbilityScore(name=score.value)
        return score_dict
