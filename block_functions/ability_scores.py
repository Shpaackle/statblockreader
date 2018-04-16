import math

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

    def add_bonus(self, args=None):
        if self.name:
            ...
        if args:
            for arg in args:
                print(arg)
