from collections import OrderedDict
from enum import Enum
from typing import Dict

import block_functions.bonuses as bonuses
from block_functions.ability_scores import AbilityScore
from block_functions.races import Race


class BONUSES(Enum):
    BAB = bonuses.BaseAttackBonus()
    Racial = bonuses.RacialBonus()
    Dodge = bonuses.DodgeBonus()
    Untyped = bonuses.UntypedBonus()
    EMPTY = bonuses.Bonus()

    @staticmethod
    def create_bonus(bonus_type=None, **kwargs):
        if not bonus_type:
            return BONUSES.EMPTY
        else:
            bonus = bonus_type

        for k, v in kwargs.items():
            bonus.k = v

        return bonus


class RACES(Enum):
    GNOME = Race(
        name="gnome",
        size="small",
        race_type="humanoid",
        race_subtype="gnome",
        auto_lang=["Lang.COMMON", "Lang.GNOME", "Lang.SYLVAN"],
        senses=["low-light vision"],
        speed_base=20,
        bonuses={
            "ability score": [
                "BONUSES.Racial.add_bonus(modifies=AbilityScores.STR, amount=-2)",
                "BONUSES.Racial.add_bonus(modifies=AbilityScores.CON, amount=2)",
                "BONUSES.Racial.add_bonus(modifies=AbilityScores.CHA, amount=2)",
            ]
        },
        traits={
            "Keen Senses": {"bonus_type": BONUSES.Racial, "source": "Keen Senses"},
            "Obsessive": {"bonus_type": BONUSES.Racial, "source": "Obsessive"},
            "Illusion Resistance": {"bonus_type": BONUSES.Racial, "source": "Illusion Resistance"},
            "Hatred": {"bonus_type": BONUSES.Untyped, "source": "Hatred"},
            "Defensive Training": {"bonus_type": BONUSES.Dodge, "source": "Defensive Training"},
            "ability scores": [
                [BONUSES.Racial, {"modifies": "STR", "amount": -2, }],
                [BONUSES.Racial, {"modifies": "CON", "amount": 2, }],
                [BONUSES.Racial, {"modifies": "CHA", "amount": 2, }],
            ],
        },
    )


class AbilityScores(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"
    EMPTY = "EMPTY"

    # creates ability scores for character
    @staticmethod
    def create_ability_scores():
        scores = OrderedDict()
        for score in AbilityScores:
            if score.name != "EMPTY":
                scores[score] = AbilityScore(name=score.value)
        return scores


class Character:
    def __init__(self, block: Dict[str, str]=None):
        self.block = block if block else {}  # TODO: raise exception
        self.race = block["race"]
        self.name = block["name"]
        self.classes = []
        self.alignment = block["alignment"]
        self.size = block["size"]
        self.skills = {}
        self.saves = {}
        self.bonuses = {}
        self.scores = {}
        self.CR = block["cr"]
        self.age = block.get("age", None)
        self.gender = block.get("gender", None)
        self.XP = block["xp"]

    def assign_race(self, name: str):
        print("name = " + str(name))
        new_race = RACES[name.upper()]
        self.race = new_race.value
        print(new_race.value.name)
