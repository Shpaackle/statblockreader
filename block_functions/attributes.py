import math
from collections import OrderedDict
from enum import Enum

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


class Attribute:
    """
    Generic base class to represent an attribute for the character
    """
    def __init__(
            self,
            name="",
            base=-999,
    ):
        self.name = name
        self.base = base
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
        return f"{self.__class__.__name__}({self.name}, {self.total})"


class AbilityScore(Attribute):
    """
    Used to represent ability scores for character
    """

    def __init__(self, name=None, base=10):
        super().__init__(name=name, base=base)
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
    def __init__(self, ability, base=10, block=dict):
        super(ArmorClass, self).__init__(name="Armor Class", base=base)
        self.ability = ability
        self.flat = base
        self.touch = base
        self.total = base
        self.bonuses = {
            "ability modifier": {"total": 0},
            "armor": {"total": 0},
            "dodge": {"total": 0},
            "shield": {"total": 0},
            "size": {"total": 0}
        }
        self.block = block

    def update_total(self):
        bonuses_values = [int(v["total"]) for v in self.bonuses.values()]
        self.total = self.base + sum(bonuses_values)


class HitPoints(Attribute):
    def __init__(self, ability, block=None,):
        super(HitPoints, self).__init__(name="Hit Points",)
        self.hit_dice = []
        self.ability = ability
        self.block = block


class Speed(Attribute):
    def __init__(self, block):
        super(Speed, self).__init__(name="Speed",)
        self.block = int(block)


class CMB(Attribute):
    def __init__(self, ability,):
        super(CMB, self).__init__(name="Combat Maneuver Bonus", base=0,)
        self.ability = ability.value


class CMD(Attribute):
    def __init__(self):
        super(CMD, self).__init__(name="Combat Maneuver Defense", base=0,)


class Save(Attribute):
    def __init__(self, name, ability,):
        super(Save, self).__init__(name, base=0,)
        self.ability = ability
        self.extras = {}


class BaseAttackBonus(Attribute):
    def __init__(self, ability):
        super(BaseAttackBonus, self).__init__(name="Base Attack Bonus", base=0,)
        self.ability = ability.value


class Skill(Attribute):
    def __init__(self, scores, name, ability, subtype=False, armor_check=False, trained_only=False):
        super(Skill, self).__init__(name)
        if ability:
            self.ability = scores[ability]
        else:
            ...  # TODO: Throw exception
        self.subtype = subtype
        self.ranks = [0]
        self.class_skill = False
        self.armor_check = armor_check
        self.trained_only = trained_only
        self.base = self.ability.modifier + self.class_skill + self.armor_check
        self.block = -999

    def __repr__(self):
        if self.total >= 0:
            bonus = '+'
        else:
            bonus = ''
        if self.subtype:
            subtype = f" ({self.subtype})"
        else:
            subtype = ''
        return (f"{self.__class__.__name__}("
                f"{self.name}{subtype} = {bonus}{self.total})")


class AbilityScores(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"

    # creates ability scores for object
    @staticmethod
    def get_ability_scores():
        """
        Creates an ordered dictionary of ability scores to return
        :return: Ordered dictionary of AbilityScore
        """
        scores = OrderedDict()
        for score in AbilityScores:
            scores[score.name] = AbilityScore(name=score.value)
        return scores


class Attributes(Enum):
    AC = ArmorClass
    BAB = BaseAttackBonus(ability=AbilityScores.STR)
    CMB = CMB(ability=AbilityScores.STR)
    CMD = CMD()
    HP = HitPoints
    INIT = Attribute(name="Initiative")
    SPD = Speed
    EMPTY = Attribute(name="EMPTY")

    def create_new(self):
        ...


class SAVES(Enum):
    FORT = ("Fortitude", "CON")
    REF = ("Reflex", "DEX")
    WILL = ("Will", "WIS")

    @staticmethod
    def get_saves(scores):
        saves = OrderedDict()
        for save in SAVES:
            saves[save.name] = Save(save.value[0], scores[save.value[1]])
        return saves


class SKILLS(Enum):
    Acrobatics = {"name": "Acrobatics", "ability": "DEX", "armor_check": True, }
    Craft = {"name": "Craft", "ability": "INT", "subtype": True, }
    Knowledge = {"name": "Knowledge", "ability": "INT", "subtype": True, "trained_only": True, }
    Perception = {"name": "Perception", "ability": "WIS", }
    Perform = {"name": "Perform", "ability": "CHA", "subtype": True, "trained_only": True}
    Profession = {"name": "Profession", "ability": "WIS", "subtype": True, "trained_only": True, }

    @staticmethod
    def create_skills(scores, skills):
        skill_dict = OrderedDict()
        for skill in skills:
            if SKILLS[skill] is SKILLS.Knowledge:
                ...
            elif SKILLS[skill] in [SKILLS.Craft, SKILLS.Perform, SKILLS.Profession]:
                ...
            else:
                skill_dict[SKILLS[skill].name] = Skill(scores, **SKILLS[skill].value)
        return skill_dict
