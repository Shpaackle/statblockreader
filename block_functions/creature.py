from block_functions.enums import Attributes, SKILLS, SAVES, AbilityScores, RACES, BONUSES


class Creature:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.CR = kwargs.get("CR", -999)
        self.XP = kwargs.get("XP", -999)
        self.race = kwargs.get("race", RACES.EMPTY.value)  # assign empty race class to creature
        self.classes = []
        self.levels = []
        self.alignment = kwargs.get("alignment", "")
        self.size = self.race.size  # set size based on race
        self.race_type = self.race.race_type  # set race_type based on race
        self.race_subtype = self.race.race_subtype  # set race_subtype based on race
        self.initiative = Attributes.INIT.value  # create initiative attribute by enum
        self.senses = self.race.senses  # set senses based on race
        self.skills = SKILLS.create_skills()  # create empty skills for creature
        self.armor_class = Attributes.AC.value
        self.hit_points = Attributes.HP.value
        self.fort_save = SAVES.FORT.value
        self.ref_save = SAVES.REF.value
        self.will_save = SAVES.WILL.value
        self.defensive_abilities = []
        self.speed = Attributes.SPD.value
        self.melee_attacks = []
        self.ranged_attacks = []
        self.special_attacks = []
        self.ability_scores = AbilityScores.get_ability_scores()
        self.base_attack_bonus = BONUSES.BAB.value
        self.combat_maneuver_bonus = Attributes.CMB.value
        self.combat_maneuver_defense = Attributes.CMD.value
        self.feats = []
        self.languages = []
        self.gear_combat = []
        self.gear_other = []
        self.stat_block = None
        self.bonuses = []

    @staticmethod
    def assign_race(self, race_name=RACES.GNOME):
        self.race = race_name
        self.race_type = race_name.race_type
        self.race_subtype = race_name.race_subtype
        self.size = race_name.size
        self.speed.base = race_name.speed_base
        self.senses.append(race_name.senses)
        Races.assign_racial_traits(self)

    _subtype_dict = {
        "knowledge": Skills.Knowledges[split_skill["subtype"]],
        "profession": Skills.Professions[split_skill["subtype"]],
        "craft": Skills.Crafts[split_skill["subtype"]],
        }

    def get_skills_from_block(self):
        block_list = self.block["skills"]
        for skill in block_list:
            split_skill = Skills.parse_block_skill(skill)
            skill_key = _subtype_dict.get(split_skill["subtype"], Skills[split_skill["name"]])
            self.skills[skill_key].total = skill_key.total
            self.skills[skill_key].extras = skill_key.extras


def create_from_block(block):
    creature = Creature(stat_block=block)
    return creature

"""
get race by name from database
assign race to character
set character size to race size
add auto languages to character languages
add language choices from race to available languages
for every trait in racial traits
add trait bonus to appropriate category

for every class in statblock
get class info from database
for every level of current class
    add skill points per level to total
    add hit die to total
    add level progression
set base attack bonus based on class & total levels
set saves as above
add class skills to character's skills

for every item in gear
get item info from database
multiply weight by quantity and add to encumberance
apply any bonus from item to character
"""
