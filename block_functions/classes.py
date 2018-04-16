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
