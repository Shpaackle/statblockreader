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
    def __init__(self, name="Armor Class", base=10):
        super(ArmorClass, self).__init__(name, base)
        self.flat = base
        self.touch = base
        self.total = base
        self.conditionals = []
        self.bonuses = {
            "ability modifier": "AbilityScores.DEX.mod",
            "armor": 0,
            "dodge": 0,
            "shield": 0,
            "size": 0
        }

    @property
    def update_total(self):
        return -1


class HitPoints(Attribute):
    def __init__(self):
        super(HitPoints, self).__init__(name="Hit Points")


class Speed(Attribute):
    def __init__(self):
        super(Speed, self).__init__(name="Speed")


class BaseAttackBonus(Attribute):
    def __init__(self):
        super(BaseAttackBonus, self).__init__(name="Base Attack Bonus")


class CMB(Attribute):
    def __init__(self):
        super(CMB, self).__init__(name="Combat Maneuver Bonus")
