from collections import namedtuple
from enum import Enum

base = namedtuple("Base", ("HD", "Skills", "Skill Points", "Saves", "BAB", "Spells"))

LEVEL_PROGRESSION = {
    "FIGHTER": {
        "base": "",
        1: ("Bonus feat",),
        2: ("Bonus feat", "bravery +1",),
        3: ("Armor training",),
        4: ("Bonus feat",),
        5: ("Weapon training",),
        6: ("Bonus feat", "bravery +2",),
        7: ("Armor training",),
        8: ("Bonus feat",),
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
        16: [],
        17: [],
        18: [],
        19: [],
        20: [],
    }
}


class BaseClass:
    """
    Class to represent base class for character
    """
    def __init__(
            self,
            name=None,
            hit_die=None,
            skill_pts=None,
            saves=(0, 0, 0),
            class_skills=None,
            base_attack=None,
            level_progression=None,
            max_level=20,
     ):
        self.name = name
        self.hit_die = hit_die
        self.skill_pts = skill_pts
        self.fort_save = saves[0]
        self.ref_save = saves[1]
        self.will_save = saves[2]
        self.class_skills = class_skills
        self.base_attack = base_attack
        self.level_progression = level_progression if level_progression else LEVEL_PROGRESSION[name.upper()]
        self.class_level = 0
        self.max_level = max_level


class CLASSES(Enum):
    FIGHTER = BaseClass(name="Fighter",
                        hit_die=10,
                        skill_pts=2,
                        saves=(2, 0, 0),
                        class_skills=["Handle Animal", "Swim"],
                        base_attack=1,
                        level_progression=LEVEL_PROGRESSION["FIGHTER"])
    CLERIC = "Cleric"
    ROGUE = "Rogue"
    BARD = "Bard"
    RANGER = "Ranger"
    WIZARD = "Wizard"
    SORCERER = "Sorcerer"
    BARBARIAN = "Barbarian"
    PALADIN = "Paladin"
