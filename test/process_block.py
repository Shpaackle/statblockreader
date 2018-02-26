import os
import json
import re


from test.db import connect_to_database as connect_db


class Bonus:
    def __init__(self, modifies="AC", bonus_type="armor", bonus_amount="+6"):
        pass


class Creature:
    def __init__(self, file_name):
        self.block = get_block(file_name)
        self.name = self.block["name"]
        self.AC = {}
        self.skills = {}

    def get_classes(self, block):
        return [(block["class"], block["level"]),
                (block.get("class2", None), block.get("level2", None)),
                (block.get("class3", None), block.get("level3", None))]

    def get_ability_mod(self, ability):
        return int(int((self.block[ability])-11)/2)

    def get_skill_ability(self, skill):
        return None  # skills_dict[skill]["ability"]

    def parse_skills(self):
        skill_dict = {}
        skill_reg = re.compile("(?P<name>[A-z )]+), ?(?P<subtype>\([A-z]\)), (?P<bonus>[0-9+- ]")
        for skill in self.block["skills"]:
            match = skill_reg.match(skill)
            name = match[0]
            bonus = match[-1]
            subtype = match.groupdict().get("subtype", None)
            if match:
                self.skills[match.groupdict()["name"]] = {"total": match.groupdict()["bonus"]}
            if match.groupdict().get("subtype", False):
                self.skills[match.groupdict()["name"]] = subtype
            skill_dict[name] = {"total": bonus, "subtype": subtype, "ability": self.get_ability_mod(self.get_skill_ability(name))}

        return skill_dict


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
    character = {}
    file_name = "../data/acid_terror.json"
    block = get_block(file_name)
    if not block:
        print("File did not load correctly")
        return -1
    parse_classes(get_classes(block), character)
    parse_race(block["race"], character)
    parse_skills(block["skills"], character)
    parse_feats(block["feats"], character)
    parse_equipment([block["combat gear"], block["other gear"]], character)

    check_hp(block, character)
    check_saves(block, character)


if __name__ == "__main__":
    main()
