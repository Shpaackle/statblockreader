from collections import defaultdict, OrderedDict
from typing import Dict

from block_functions.attributes import AbilityScores, SAVES, Attributes, SKILLS
from block_functions.bonuses import BONUSES
from block_functions.classes import CLASSES
from block_functions.races import RACES


class Character:
    def __init__(self, block: Dict[str, str]):
        self.block = block if block else {}  # TODO: raise exception if block is empty
        self.race = block["race"]
        self.name = block["name"]
        self.alignment = block["alignment"]
        self.size = block["size"]
        self.CR = block["cr"]
        self.age = block.get("age", "")
        self.gender = block.get("gender", "")
        self.XP = block["xp"]
        self.scores = AbilityScores.get_ability_scores()
        self.saves = SAVES.get_saves(self.scores)
        self.skills = SKILLS.create_skills(self.scores, ["Acrobatics", "Perception"])
        self.AC = Attributes.AC.value(self.scores["DEX"], block=block.get("ac", dict()))
        self.HP = Attributes.HP.value(self.scores["CON"], block={"hp": block["hp"], "hitdice": block["hitdice"]})
        self.speed = Attributes.SPD.value(block=block["speed"])
        self.classes = {}
        self.bonuses = defaultdict(list)
        self.skill_points = 0
        self.hit_dice = OrderedDict([(4, 0), (6, 0), (8, 0), (10, 0), (12, 0)])
        self.armor_check_penalty = BONUSES.untyped.value(bonus_type="armor check",
                                                         source="armor check penalty",
                                                         amount=0,
                                                         penalty=True, )

    def assign_race(self, name: str):
        """
        Creates new race from RACES enum based on name. Then assigns it to character
        :param name: name of race from stat block, used as reference for RACES enum\\\\\\\\
        """
        new_race = RACES[name.upper()]
        self.race = new_race.value

        for trait in iter(self.race.traits):
            bonus = BONUSES.create_bonus(
                bonus_type=trait.type,
                name=trait.name,
                source=trait.source,
                modifies=trait.bonus.modifies,
                amount=trait.bonus.amount,
                active=trait.bonus.active,
            )
            self.bonuses[trait.type].append(bonus)

    def assign_classes(self, names: list, ):
        """
        :param names: list of names of class from stat block to use as reference for CLASSES enum
        """
        classes = OrderedDict()  # create empty ordered dict to hold classes
        for name in names:  # iterate through names in list
            _class = CLASSES[name.upper()]  # assign class from CLASSES
            classes[_class.name] = _class.value
            levels = []  # TODO: fill in with levels from stat block
            for level in levels:
                classes[name.upper()].class_level = level
                self.assign_levels(name, level)

        self.classes = classes

    def assign_levels(self, _class: str, levels: int):
        LP = self.classes[_class.upper()].level_progression
        for level in range(levels + 1):
            self.hit_dice[self.classes[_class.upper()].hit_die] += 1
            self.skill_points += 0
