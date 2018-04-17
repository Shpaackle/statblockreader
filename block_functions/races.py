from enum import Enum


class Race:
    """
    Class to represent race of character
    """
    def __init__(self, **kwargs):
        self.name = ""
        self.size = None
        self.race_type = ""
        self.race_subtype = ""
        self.auto_lang = []
        self.senses = []
        self.speed_base = -999
        self.bonuses = {}
        self.traits = {}

        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)


class RACES(Enum):
    GNOME = Race(
        name="gnome",
        size="small",
        race_type="humanoid",
        race_subtype="gnome",
        auto_lang=["Common", "Gnome", "Sylvan"],
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
            "Keen Senses": {"bonus_type": "racial", "source": "Keen Senses"},
            "Obsessive": {"bonus_type": "racial", "source": "Obsessive"},
            "Illusion Resistance": {"bonus_type": "racial", "source": "Illusion Resistance"},
            "Hatred": {"bonus_type": "untyped", "source": "Hatred"},
            "Defensive Training": {"bonus_type": "dodge", "source": "Defensive Training"},
            "ability scores": [
                ["racial", {"modifies": "STR", "amount": -2, }],
                ["racial", {"modifies": "CON", "amount": 2, }],
                ["racial", {"modifies": "CHA", "amount": 2, }],
            ],
        },
    )


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
                "BONUSES.Racial.add_bonus(modifies=AbilityScores.CHA, amount=2)",
            ]
        }
        self.racial_traits = {
            "ability score": [
                ["racial", {"modifies": "AbilityScores.STR", "amount": -2, }],
                ["racial", {"modifies": "AbilityScores.CON", "amount": 2, }],
                ["racial", {"modifies": "AbilityScores.CHA", "amount": 2, }],
            ],
            "Keen Senses": {"bonus_type": "BONUSES.Racial", "source": "Keen Senses"},
            "Obsessive": {"bonus_type": "BONUSES.Racial", "source": "Obsessive"},
            "Illusion Resistance": {"bonus_type": "BONUSES.Racial", "source": "Illusion Resistance"},
            "Hatred": {"bonus_type": "BONUSES.Untyped", "source": "Hatred"},
            "Defensive Training": {"bonus_type": "BONUSES.Dodge", "source": "Defensive Training"}}


def assign_race_bonuses(creature):
    ...


def assign_racial_traits(creature):
    """
    for trait_name, trait_value in creature.race.racial_traits.items():
        if trait_name == "ability score":
            for bonus in trait_value:
                new_bonus = BONUSES.create_bonus(bonus["type"], bonus["modifies"])
                # creature.bonuses.append(BONUSES.new_bonus(bonus[0], **kwargs=[bonus[1:] + source=trait_name],))
                ...
        else:
            # creature.bonuses.append(BONUSES.new_bonus(bonus[0], **kwargs=[bonus[1:] + source=trait_name]
            ...
    """
    ...
