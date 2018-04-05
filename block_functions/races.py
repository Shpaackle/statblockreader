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
			"ability score": [
                [bonus_type=Bonuses.Racial, modifies=AbilityScores.STR, amount=-2,],
                [bonus_type=Bonuses.Racial, modifies=AbilityScores.CON, amount=2,],
                [bonus_type=Bonuses.Racial, modifies=AbilityScores.CHA, amount=2,],
				],
            "Keen Senses": [bonus_type=Bonuses.Racial, source="Keen Senses"]
            "Obsessive": [bonus_type=Bonuses.Racial, source="Obsessive"],
            "Illusion Resistance": [bonus_type=Bonuses.Racial, source="Illusion Resistance"],
            "Hatred": [bonus_type=Bonuses.Untyped, source="Hatred"],
            "Defensive Training": [bonus_type=Bonuses.Dodge, source="Defensive Training"]
        }


def assign_race_bonuses(creature):
	...

def assign_racial_traits(creature):
	for trait_name, trait_value in creature.race.racial_traits.items():
		if trait_name == "ability score":
			for bonus in trait_value:
				creature.bonuses.append(
					Bonuses.new_bonus(bonus_type=bonus[0],
									  **kwargs=[bonus[1:] + source=trait_name],
									  )
				)
		else:
			creature.bonuses.append(Bonuses.new_bonus(bonus_type=bonus[0],
													  **kwargs=[bonus[1:] + source=trait_name]


class Races(Enum):
    GNOME = Gnome()
    EMPTY = Race()
