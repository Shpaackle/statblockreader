from enum import Enum
from typing import Dict

import block_functions.bonuses as bonuses
from block_functions.attributes import AbilityScores, SAVES, Attributes, SKILLS
from block_functions.races import RACES


class BONUSES(Enum):
    BAB = bonuses.BaseAttackBonus()
    Racial = bonuses.RacialBonus()
    Dodge = bonuses.DodgeBonus()
    Untyped = bonuses.UntypedBonus()
    EMPTY = bonuses.Bonus()

    @staticmethod
    def create_bonus(bonus_type=None, **kwargs):
        if not bonus_type:
            # TODO: Throw Error instead of returning empty bonus
            return BONUSES.EMPTY
        else:
            bonus = bonus_type

        for k, v in kwargs.items():
            setattr(bonus, k, v)

        return bonus


class Character:
    def __init__(self, block: Dict[str, str]):
        self.block = block if block else {}  # TODO: raise exception if block is empty
        self.race = block["race"]
        self.name = block["name"]
        self.alignment = block["alignment"]
        self.size = block["size"]
        self.CR = block["cr"]
        self.age = block.get("age", None)
        self.gender = block.get("gender", None)
        self.XP = block["xp"]
        self.scores = AbilityScores.get_ability_scores()
        self.saves = SAVES.get_saves(self.scores)
        self.skills = SKILLS.create_skills(self.scores, ["Acrobatics", "Perception"])
        self.AC = Attributes.AC.value
        self.HP = Attributes.HP.value(self.scores["CON"], block={"hp": block["hp"], "hitdice": block["hitdice"]})
        self.classes = []
        self.bonuses = {}
        self.armor_check_penalty = 0

    def assign_race(self, name: str):
        """
        Creates new race from RACES enum based on name. Then assigns it to character
        :param name: name of race from stat block, used as reference for RACES enum
        """
        new_race = RACES[name.upper()]
        self.race = new_race.value
