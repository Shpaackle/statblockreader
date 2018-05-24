import json
import math
import pprint
import re

from .db import connect_to_database as connect_db


class Attribute:
    def __init__(self, name, base=-1):
        self.name = name
        self.base = base
        self.bonuses = {}  # keys are type of bonus, list of current bonuses as values
        self.total = self.base

    def set_base(self, amount):
        self.base = amount

    def remove_bonus(self, bonus_removed):
        pass

    def find_bonus_type(self, bonus_type):
        pass

    def add_bonus(self, new_bonus):
        # check if bonus type already exists
        if self.bonuses.get(new_bonus.kind, False):
            if new_bonus.is_stackable:
                self.bonuses[new_bonus.kind].append(new_bonus)
            """
            for bonus in bonuses.:
                if bonus.source == new_bonus.source:
                    same = True
                    exists = True
                    break
                elif (bonus.kind == new_bonus.kind):
                    if bonus.is_stackable || new_bonus.is_stackable:
                        bonuses.append()
                    if bonus.amount > 0:
                        pass
                        if new_bonus.amount > bonus.amount:
                            pass
                    elif bonus.amount < 0:
                        pass
            """

    def set_total(self):
        temp = self.base
        for key in self.bonuses.keys():
            for bonus in self.bonuses[key]:
                if bonus.add_to_total:
                    temp += bonus.amount
            pass


class AbilityScore(Attribute):
    def __init__(self, name, base=-1):
        super().__init__(name, base)
        self.point_buy_cost = 0

    def get_modifier(self):
        pass


class Skill(Attribute):
    def __init__(self, db_skill, base=-1, ranks=0, ):
        super().__init__(db_skill.name, base)
        self.key_ability = db_skill.ability
        self.ranks = ranks
        self.untrained = db_skill.untrained
        self.armor_check = db_skill.armor_check
        if db_skill.subtype:
            self.subtype = db_skill.subtype
        self.is_class_skill = False
        self.special = []

    def __str__(self):
        message = "{}  +{} = {} + {}".format(self.name, self.base, self.ranks, self.key_ability)
        return message

    def toggle_class_skill(self):
        self.is_class_skill = not self.is_class_skill

    def add_ranks(self, amount):
        self.ranks += amount

    def remove_ranks(self, amount):
        self.ranks -= amount


class Race:
    def __init__(self, name, main_type, subtype=None):
        self.name = name
        self.main_type = main_type
        self.subtype = subtype
        self.granted_abilities = {}
        self.size = None
        self.speed = None
        self.languages = []
        self.senses = []


class Bonus:
    def __init__(self, source="Breastplate", modifies="AC", bonus_type="armor", amount: any =6, duration=-1,
                 is_stackable=False):
        self.source = source
        self.modifies = modifies
        self.bonus_type = bonus_type
        try:
            if (amount[0] == '+') or (amount[0] == '-'):
                self.amount = int(amount[1:].strip())
            elif amount[0].isdigit():
                self.amount = amount.strip()
        except ValueError:
            self.amount = amount
        self.duration = duration
        self.is_stackable = is_stackable
        self.add_to_total = False

    def change_amount(self, amount):
        self.amount = amount


class Class:
    def __init__(self, db_class):
        self.name = db_class.name
        self.hit_die = db_class.hit_die
        self.skill_points = db_class.skill_points
        self.alignment = db_class.alignment
        self.abilities = []
        self.class_skills = {}
        self.spells_per_day = None
        self.spells_known = []
        self.saves = []
        self.is_prestige = db_class.is_prestige
        self.is_favored = False
        self.favored_bonus = None


def get_block(file_name):
    """
    check if json file
    then open json and return file
    otherwise, return None
    """
    pprint.pprint(file_name)
    data_folder = '../data/'
    try:
        with open(data_folder + file_name) as f:
            # grab all lines of statblock
            return json.load(f)
    except TypeError:
        return file_name


class Creature:
    def __init__(self, file_name):
        self.block = get_block(file_name)
        self.name = self.block["name"]
        self.AC = {}
        self.skills = {}
        self.race = None
        self.abilities = {"Str": 14,
                          "Dex": 16,
                          "Con": 18,
                          "Int": 12,
                          "Wis": 15,
                          "Cha": 10
                          }
        self.feats = {}
        self.encumbrance = {"weight": {"total": 0, "sum": []}, "max_load": None, "light_load": None,
                            "medium_load": None, "heavy_load": None}
        self.armor_check_penalty = {"total": 0, "armor": 0, "encumbrance": 0}

    def assign_race(self):
        pass

    def get_classes(self):
        return [(self.block["class"], self.block["level"]),
                (self.block.get("class2", None), self.block.get("level2", None)),
                (self.block.get("class3", None), self.block.get("level3", None))]

    @staticmethod
    def get_ability_mod(ability):
        return math.floor((ability.total - 10) / 2)

    def parse_skills(self):
    	"""
    	
    	"""
        skill_dict = {}
        skill_reg = re.compile("(?P<name>[A-z ]*) ?(?P<subtype>[A-z() ]+)? (?P<bonus>[0-9+-]+)")
        for skill in self.block["skills"]:
            match = skill_reg.match(skill)
            name = match.groupdict().get("name")
            bonus = match.groupdict().get("bonus")
            subtype = match.groupdict().get("subtype", None)
            if match:
                self.skills[match.groupdict()["name"]] = {"total": match.groupdict()["bonus"]}
            if subtype:
                self.skills[match.groupdict()["name"]]["subtype"] = match.groupdict()["subtype"]
            skill_dict[name] = {"total": bonus, "subtype": subtype, "ability": "TEST"}

        return skill_dict

	def get_skill_totals(self):
		"""
		for every skill in self.skills
			SET temp_total to 0
			SET ability_mod to current skill's key_ability mod
			ADD ability_mod to temp_total
			ADD ranks to temp_total
			GET all_bonuses from skill.bonuses
			FOR every bonus_type in all_bonuses
				SET max_bonus, type_total to 0
				FOR every bonus in bonus_type
					IF stackable
						ADD bonus amount to temp_total
						ADD bonus amount to type_total
					ELIF bonus amount > 0 and > max_bonus
						SET max_bonus to bonus amount
						SET type_total to bonus amount
					ELIF bonus amount < 0 and < max_bonus
						IF max_bonus > 0
							ADD bonus amount to temp_total
						ELSE 
							SET max bonus to bonus amount
						ADD bonus amount to type_total
					ADD max_bonus to temp_total
				SET bonus_type.total to type_total
			SET skill total to temp total
		"""


class Feat:
    def __init__(self, name, category, subcategory=None, description=None, prereqs=None):
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.description = description
        self.prereqs = prereqs
        self.is_bonus = False

    def check_prerequisites(self, character):
        pass


class BlockError:
    pass


def parse_classes(block_classes, character):
    pass


def parse_race(block_race, character):
    pass


def parse_feats(block_feats, character):
    pass


def parse_equipment(block_gear, character):
    pass


def check_hp(block_hp, character):
    pass


def check_saves(block_saves, character):
    pass


SAVES_DICT = {"classes": [],
              "ability mod": None,
              "gear": None,
              "racial": None,
              "feats": None,
              "other": []
              }
CLASSES_DICT = {}
RACE_DICT = {}
ABILITY_SCORES_DICT = {"base": [],  # integer plus point buy value
                       "race": [],
                       "levels": [],  # index is levels/4 - 1
                       "gear": []
                       }
HP_DICT = {}
FEATS_DICT = {}
SKILLS_DICT = {"classes": [],
               "ability mod": None,
               "gear": [],
               "racial": [],
               "feats": None,
               "other": []
               }
AC_DICT = {"base": 10,
           "armor": None,
           "deflection": None,
           "size": None,
           }
BONUS_TYPES = {
    "alchemical": False,
    "armor": False,
    "base attack bonus": False,
    "circumstance": True,
    "competence": False,
    "deflection": False,
    "dodge": True,
    "enhancement": False,
    "inherent": False,
    "insight": True,
    "luck": False,
    "morale": False,
    "natural armor": False,
    "profane": False,
    "racial": False,
    "resistance": False,
    "sacred": False,
    "shield": False,
    "size": True,
    "trait": False
}


def test_skills(character):
    class TestSkill:
        def __init__(self, name, ability, untrained, armor_check, subtype=False):
            self.name = name
            self.ability = ability
            self.untrained = untrained
            self.armor_check = armor_check
            self.subtype = subtype

    stealth = TestSkill("Stealth", "Dex", True, True)
    perception = TestSkill("Perception", "Wis", True, False)
    character.skills["Stealth"] = Skill(stealth, base=18, ranks=6)
    character.skills["Perception"] = Skill(perception, base=28, ranks=19)
    character.get_skill_totals()


gnome = {
    "name": "gnome",
    "race_type": "humanoid",
    "race_subtype": "gnome",
    "racial traits": {
        "ability score modifiers": [Bonus(source="gnome racial traits", modifies="CON", bonus_type="racial",
                                          amount=2, duration=-1, is_stackable=False),
                                    Bonus(source="gnome racial traits", modifies="CHA", bonus_type="racial",
                                          amount=2, duration=-1, is_stackable=False),
                                    Bonus(source="gnome racial traits", modifies="STR", bonus_type="racial",
                                          amount=-2, duration=-1, is_stackable=False)],
        "small": [Bonus(source="small size", modifies="AC", bonus_type="size", amount=1),
                  Bonus(source="small size", modifies="ATK", bonus_type="size", amount=1),
                  Bonus(source="small size", modifies="CMB", bonus_type="untyped", amount=-1, is_stackable=True),
                  Bonus(source="small size", modifies="CMD", bonus_type="untyped", amount=-1, is_stackable=True),
                  Bonus(source="small size", modifies="SKILL:Stealth", bonus_type="size", amount=4)],
        "slow speed": Attribute("speed", base=20),
        "low-light vision": {"senses": "low-light vision"},
        "defensive training": {}
    }
}


def iterate_block():
    # Initialize iteration of block

    ...


def main():
    database = connect_db()
    items = database.items
    file_name = "ageless_master.json"
    character = Creature(file_name)
    parse_classes(character.get_classes(), character)
    parse_race(character.block["race"], character)
    character.parse_skills()
    parse_feats(character.block["feats"], character)
    parse_equipment([character.block["combat gear"], character.block["other gear"]], character)

    check_hp(character.block, character)
    check_saves(character.block, character)

    pprint.pprint(character.name)
    pprint.pprint(character.skills)

    test_skills(character)


if __name__ == "__main__":
    main()
