from block_functions import races as Races
from block_functions import saves as Saves
from block_functions.ability_scores import AbilityScores
from block_functions.attributes import Attributes
from block_functions.bonuses import Bonuses
from block_functions.skills import Skills


class Creature:
    def __init__(self):
        self.name = ""
        self.CR = -999
        self.XP = -999
        self.race = Races.Races.EMPTY.value
        self.classes = []
        self.levels = []
        self.alignment = ""
        self.size = self.race.size
        self.race_type = self.race.race_type
        self.race_subtype = self.race.race_subtype
        self.initiative = Attributes.Initiative.value
        self.senses = self.race.senses
        self.skills = Skills.create_skills()
        self.armor_class = Attributes.AC.value
        self.hit_points = Attributes.HP.value
        self.fort_save = Saves.Save(name="Fortitude")
        self.ref_save = Saves.Save(name="Reflex")
        self.will_save = Saves.Save(name="Will")
        self.defensive_abilities = []
        self.speed = Attributes.Speed.value
        self.melee_attacks = []
        self.ranged_attacks = []
        self.special_attacks = []
        self.ability_scores = AbilityScores.get_ability_scores()
        self.base_attack_bonus = Bonuses.BAB.value
        self.combat_maneuver_bonus = Attributes.CMB.value
        self.combat_maneuver_defense = Attributes.CMD.value
        self.feats = []
        self.languages = []
        self.gear_combat = []
        self.gear_other = []
        self.stat_block = None

    @staticmethod
    def assign_race(self, race_name=Races.Races.GNOME):
        self.race = race_name


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
