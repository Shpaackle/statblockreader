from collections import namedtuple
from enum import Enum


class Race:
    """
    Class to represent race of character
    """
    def __init__(self, **kwargs,):
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


Bonus = namedtuple("Bonus", ("modifies", "amount", "active"))
Trait = namedtuple("Trait", ("name", "type", "source", "bonus", "description",))


class RACES(Enum):
    GNOME = Race(
        name="gnome",
        size="small",
        race_type="humanoid",
        race_subtype="gnome",
        auto_lang=["Common", "Gnome", "Sylvan"],
        senses=["low-light vision"],
        speed_base=20,
        bonuses={},
        traits=(
            Trait("Keen Senses", "racial", "RACES.Gnome", Bonus("Perception", 2, True),
                  "description",),
            Trait("Obsessive", "racial", "RACES.Gnome", Bonus("bonus", 0, True), "description",),
            Trait("Illusion Resistance", "racial", "RACES.Gnome", Bonus("bonus", 0, True), "description",),
            Trait("Hatred", "untyped", "RACES.Gnome", Bonus("bonus", 0, True), "description",),
            Trait("Defensive Training", "dodge", "RACES.Gnome", Bonus("bonus", 0, True), "description",),
            Trait("STR", "racial", "RACES.Gnome", Bonus("STR", -2, True), "description",),
            Trait("CON", "racial", "RACES.Gnome", Bonus("CON", 2, True), "description", ),
            Trait("CHA", "racial", "RACES.Gnome", Bonus("CHA", 2, True), "description", ),
        ),
    )

    @staticmethod
    def bonus_kwargs(trait):
        b_type = "Untyped"
        bonus = {
            "name": "",
            "source": "",
            "modifies": "",
            "amount": "",
            "active": True,
            "stackable": False,
        }
        return b_type, bonus


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
