import os
import json
import re
import math

from testing.db import connect_to_database as connect_db


class Attribute:
    def __init__(self, name, base=-1):
        self.name = name
        self.base = base
        self.bonuses = {}
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
        self.name = name
        self.base = base
        self.bonuses = {}
        self.total = base


    def get_modifier(self):
        pass


class Skill(Attribute):
    def __init__(self, name, ability, base=-1):
        self.key_ability = ability
        super(Attribute, self).__init__(name, base)

    def add_ranks(self, amount):
        self.rank += amount

    def remove_ranks(self, amount):
        self.rank -= amount


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
    def __init__(self, source="Breastplate", modifies="AC", kind="armor", amount=6, duration=-1, is_stackable=False):
        self.source = source
        self.modifies = modifies
        self.kind = kind
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


def get_block(file_name):
    """
    check if json file
    then open json and return file
    otherwise, return None
    """
    if os.path.splitext(file_name)[1] == ".json":
        file = open(file_name)
        return json.load(file)
    else:
        return None


class Creature:
    def __init__(self, file_name):
        self.block = get_block(file_name)
        self.name = self.block["name"]
        self.AC = {}
        self.skills = {}
        self.race = None
        self.abilities = {}
        self.feats = {}

    def assign_race(self):
        pass

    def get_classes(self, block):
        return [(block["class"], block["level"]),
                (block.get("class2", None), block.get("level2", None)),
                (block.get("class3", None), block.get("level3", None))]

    def get_ability_mod(self, ability):
        return math.floor()

    def parse_skills(self):
        skill_dict = {}
        skill_reg = re.compile("(?P<name>[A-z )]+), ?(?P<subtype>\([A-z()]\)), (?P<bonus>[0-9+-])")
        for skill in self.block[self.skills]:
            match = skill_reg.match(skill)
            name = match[0]
            bonus = match[-1]
            subtype = match.groupdict().get("subtype", None)
            if match:
                self.skills[match.groupdict()["name"]] = {"total": match.groupdict()["bonus"]}
            if match.groupdict().get("subtype", False):
                self.skills[match.groupdict()["name"]]
            skill_dict[name] = {"total": bonus, "subtype": subtype, "ability": self.get_ability_mod(self.get_skill_ability(name))}

        return skill_dict



class Feat:
    def __init__(self, name, category, subcategory=None, description=None, prereqs=None):
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.description = description
        self.prereqs = prereqs
        self.is_bonus = False

    def check_prereqs(self, character):
        pass


class BlockError():
    pass


def parse_classes(block_classes, character):
    pass


def parse_race(block_race, character):
    pass


def parse_skills(block_skills, character):
    pass


def parse_feats(block_feats, character):
    pass


def parse_equipment(block_gear, character):
    pass


def check_hp(block_hp, character):
    pass


def check_saves(block_saves, character):
    pass


DATABASE = None
SAVES_DICT = {"classes": [],
              "ability mod": None,
              "gear": None,
              "racial": None,
              "feats": None,
              "other": []
}
CLASSES_DICT = {}
RACE_DICT = {}
ABILITY_SCORES_DICT = {"base": [], # integer plus point buy value
                       "race": [],
                       "levels": [], # index is levels/4 - 1
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
BONUS_TYPES= {
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


def main():
    DATABASE = connect_db()
    items = DATABASE.items
    file_name = "../data/acid_terror.json"
    block = get_block(file_name)
    if not block:
        print("File did not load correctly")
        return -1
    character = Creature(block)
    parse_classes(character.get_classes(block), character)
    parse_race(block["race"], character)
    parse_skills(block["skills"], character)
    parse_feats(block["feats"], character)
    parse_equipment([block["combat gear"], block["other gear"]], character)

    check_hp(block, character)
    check_saves(block, character)


if __name__ == "__main__":
    main()
