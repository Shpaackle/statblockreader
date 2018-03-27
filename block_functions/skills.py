from .attributes import Attribute
from enum import Enum
from .ability_scores import AbilityScores


class Skill(Attribute):
    def __init__(self, name=None, ability=None):
        super(Attribute).__init__(name, ability)
        self.ranks = [0]
        self.class_skill = False
        self.armor_check = False
        self.trained_only = False
        self.base = self.ability.modifier


class Skills(Enum):
    Perception = Skill(name="Perception", ability=AbilityScores.WIS.name)


def create_skills():
    skill_dict = {}
    for skill in Skills:
        skill_dict[skill.name] = skill.value
    return skill_dict
