from enum import Enum

from block_functions.bonuses import Bonuses


class Race:
    def __init__(self):
        self.name = ""
        self.size = None
        self.race_type = ""
        self.race_subtype = ""
        self.auto_lang = []
        self.senses = []
        self.speed_base = -999
        self.bonuses = {}
        self.racial_traits = {}


class Gnome(Race):
    def __init__(self):
        super(Gnome, self).__init__()
        self.name = "gnome"
        self.size = "Sizes.SMALL"
        self.race_type = "humanoid"
        self.race_subtype = "gnome"
        self.auto_lang = ["Lang.COMMON", "Lang.GNOME", "Lang.SYLVAN"]
        self.senses = ["low-light vision"]
        self.speed_base = 20
        self.bonuses = {
            "ability score": [
                "BONUSES.Racial.add_bonus(modifies=AbilityScores.STR, amount=-2)",
                "BONUSES.Racial.add_bonus(modifies=AbilityScores.CON, amount=2)",
                "BONUSES.Racial.add_bonus(modifies=AbilityScores.CHA, amount=2)"]
        }
        self.racial_traits = {
            "Keen Senses": Bonuses.create_bonus(bonus_type=Bonuses.Racial, source="Keen Senses"),
            "Obsessive": Bonuses.create_bonus(bonus_type=Bonuses.Racial, source="Obsessive"),
            "Illusion Resistance": Bonuses.create_bonus(bonus_type=Bonuses.Racial, source="Illusion Resistance"),
            "Hatred": Bonuses.create_bonus(bonus_type=Bonuses.Untyped, source="Hatred"),
            "Defensive Training": Bonuses.create_bonus(bonus_type=Bonuses.Dodge, source="Defensive Training")
        }


class RACES(Enum):
    GNOME = Gnome()
    EMPTY = Race()
