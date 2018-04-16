from collections import OrderedDict
from enum import Enum

from block_functions.attributes import Attribute, Speed, CMB, CMD, HitPoints, ArmorClass, AbilityScore
from block_functions.bonuses import BaseAttackBonus, RacialBonus, DodgeBonus, UntypedBonus, Bonus
from block_functions.classes import BaseClass
from block_functions.feats import Feat
from block_functions.items import Item
from block_functions.races import Gnome, Race
from block_functions.saves import Save


#from block_functions.skills import Knowledges, Skill


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


class Attributes(Enum):
    INIT = Attribute(name="Initiative")
    SPD = Speed()
    CMB = CMB(ability=AbilityScores.STR)
    CMD = CMD()
    HP = HitPoints(ability=AbilityScores.CON)
    AC = ArmorClass(ability=AbilityScores.DEX)
    EMPTY = Attribute(name="EMPTY")

    def create_new(self):
        ...


class SKILLS(Enum):
    Perception = "Perception"
    Knowledge = {
        "arcana": Knowledges.arcana
    }

    @staticmethod
    def create_skills():
        skill_dict = OrderedDict()
        for skill in SKILLS:
            skill_dict[skill] = Skill(skill.value)
        return skill_dict


class SAVES(Enum):
    FORT = Save(name="Fortitude")
    REF = Save(name="Reflex")
    WILL = Save(name="Will")
    EMPTY = Save(name="EMPTY")


class CLASSES(Enum):
    FIGHTER = BaseClass(name="Fighter")
    BARD = BaseClass(name="Bard")


class RACES(Enum):
    GNOME = Gnome()
    EMPTY = Race()


class Items(Enum):
    Rapier = Item(name="Rapier")
    EMPTY = Item(name="EMPTY")


class BONUSES(Enum):
    BAB = BaseAttackBonus()
    Racial = RacialBonus()
    Dodge = DodgeBonus()
    Untyped = UntypedBonus()
    EMPTY = Bonus()

    @staticmethod
    def create_bonus(bonus_type=None, **kwargs):
        if not bonus_type:
            return BONUSES.EMPTY
        else:
            bonus = bonus_type

        for k, v in kwargs.items():
            bonus.k = v

        return bonus


class FEATS(Enum):
    WeaponFinesse = Feat()
    Dodge = Feat()
    Mobility = Feat()
    EMPTY = Feat()
