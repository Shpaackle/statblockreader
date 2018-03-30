from collections import OrderedDict
from enum import Enum

from block_functions.attributes import Attribute
from .ability_scores import AbilityScores


class Skill(Attribute):
    def __init__(self, name=None, ability=AbilityScores.EMPTY):
        super(Attribute, self).__init__()
        self.name = name
        self.ability = ability.value
        self.ranks = [0]
        self.class_skill = False
        self.armor_check = False
        self.trained_only = False
        self.base = self.ability.modifier + self.class_skill + self.armor_check


class Knowledges(Enum):
    arcana = Skill(name="Knowledge (arcana)", ability=AbilityScores.INT)


class Skills(Enum):
    Perception = Skill(name="Perception", ability=AbilityScores.WIS)
    Knowledge = {
        "arcana": Knowledges.arcana
    }

    @staticmethod
    def create_skills():
        skill_dict = {}
        for skill in Skills:
            skill_dict[skill.name] = skill.value
        return OrderedDict([])
