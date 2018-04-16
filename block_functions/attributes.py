import math


class Attribute:
    def __init__(
            self,
            name="",
            ability=None,
    ):
        self.name = name
        self.ability = ability
        self.base = -999
        self.bonuses = {"total": 0}  # assign total value to 0 for all bonuses
        self.total = self.base + self.bonuses["total"]
        self.conditions = []

    def get_highest_bonus(self, bonus_type):
        """
        Find highest bonus of a particular type
        :param bonus_type: array of type of bonus to search for, including all
        :return: dictionary with type(s)
        """
        ...

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.name}, {self.total}")


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


class ArmorClass(Attribute):
    def __init__(self, ability, base=10,):
        super(ArmorClass, self).__init__(name="Armor Class")
        self.ability = ability.value
        self.base = base
        self.flat = base
        self.touch = base
        self.total = base
        self.conditionals = []
        self.bonuses = {
            "ability modifier": {"total": self.ability.modifier},
            "armor": {"total": 0},
            "dodge": {"total": 0},
            "shield": {"total": 0},
            "size": {"total": 0}
        }

    def update_total(self):
        bonuses_values = [int(v["total"]) for v in self.bonuses.values()]
        self.total = self.base + sum(bonuses_values)


class HitPoints(Attribute):
    def __init__(self, ability,):
        super(HitPoints, self).__init__(name="Hit Points")
        self.hit_dice = []
        self.ability = ability.value


class Speed(Attribute):
    def __init__(self):
        super(Speed, self).__init__(name="Speed")


class CMB(Attribute):
    def __init__(self, ability,):
        super(CMB, self).__init__(name="Combat Maneuver Bonus")
        self.ability = ability.value


class CMD(Attribute):
    def __init__(self):
        super(CMD, self).__init__(name="Combat Maneuver Defense")
