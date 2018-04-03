from enum import Enum


class Attribute:
    def __init__(self, name, ability=None):
        self.name = name
        self.base = -999
        self.bonuses = {"total": 0}  # assign total value to 0 for all bonuses
        self.total = self.base + self.bonuses["total"]
        self.ability = ability
        self.conditions = []

    @staticmethod
    def get_highest_bonus(self, bonus_type):
        """
        Find highest bonus of a particular type
        :param bonus_type: array of type of bonus to search for, including all
        :return: dictionary with type(s)
        """

        ...


class ArmorClass(Attribute):
    def __init__(self, base=10):
        from block_functions.ability_scores import AbilityScores
        super(ArmorClass, self).__init__(name="Armor Class")
        self.ability = AbilityScores.DEX.value
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
    def __init__(self):
        super(HitPoints, self).__init__(name="Hit Points")
        self.hit_dice = []
        from block_functions.ability_scores import AbilityScores
        self.ability = AbilityScores.CON


class Speed(Attribute):
    def __init__(self):
        super(Speed, self).__init__(name="Speed")


class CMB(Attribute):
    def __init__(self):
        super(CMB, self).__init__(name="Combat Maneuver Bonus")
        from block_functions.ability_scores import AbilityScores
        self.ability = AbilityScores.STR


class CMD(Attribute):
    def __init__(self):
        super(CMD, self).__init__(name="Combat Maneuver Defense")


class Attributes(Enum):
    INIT = Attribute(name="Initiative")
    SPD = Speed()
    CMB = CMB()
    CMD = CMD()
    HP = HitPoints()
    AC = ArmorClass()
    EMPTY = Attribute(name="EMPTY")
