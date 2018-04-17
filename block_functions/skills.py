from collections import OrderedDict
from enum import Enum

from block_functions.attributes import Attribute
from block_functions.enums import AbilityScores


class SKILLS(Enum):
    Acrobatics = {"name": "Acrobatics", "ability": "DEX", "armor_check": True}
    Perception = {"name": "Perception", "ability": "WIS", }
    Knowledge = {}

    @staticmethod
    def create_skills(scores):
        skill_dict = OrderedDict()
        for skill in SKILLS:
            skill_dict[skill.name] = Skill(scores, **skill.value)
        return skill_dict


class Skill(Attribute):
    def __init__(self, name=None, ability=AbilityScores.EMPTY):
        super(Attribute, self).__init__(name,)
        self.ability = ability
        self.ranks = [0]
        self.class_skill = False
        self.armor_check = False
        self.trained_only = False
        self.base = self.ability.modifier + self.class_skill + self.armor_check

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.name} = {(if self.total >= 0: '+' else: '-')} {self.total}")


class Knowledges(Enum):
    arcana = Skill(name="Knowledge (arcana)", ability=AbilityScores.INT)
