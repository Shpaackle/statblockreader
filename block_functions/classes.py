from enum import Enum

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
        self.level_progression = level_progression
        self.class_level = 0
        self.max_level = max_level

class Classes(Enum):
	FIGHTER =  BaseClass(name="Fighter", hit_die=10, skill_pts=2, saves=(2, 0, 0), class_skills=["Handle Animal", "Swim"], base_attack=1)
	CLERIC = "Cleric"
	ROGUE = "Rogue"
	BARD = "Bard"
	RANGER = "Ranger"
	WIZARD = "Wizard"
	SORCERER = "Sorcerer"
	BARBARIAN = "Barbarian"
	PALADIN = "Paladin"
