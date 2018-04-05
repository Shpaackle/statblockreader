"""
    # basic class for things like
    #   Strength, Fortitude, Armor Class
    class Attribute:
        def __init__(self, name, ability=None):
            self.name = name
            self.base = -999
            self.bonuses = {"total": 0}  # assign total value to 0 for all bonuses
            self.total = self.base + self.bonuses["total"]
            self.ability = ability
            self.conditions = []
    
        @staticmethod
        def get_highest_bonus(self, bonus_type):
            '''
            Find highest bonus of a particular type
            :param bonus_type: array of type of bonus to search for, including all
            :return: dictionary with type(s)
            '''
            ...
    
    
    class Bonus:
        def __init__(self, source=None, modifies=None, amount=None, duration=None, bonus_type=None, stackable=False):
            self.source = source
            self.modifies = modifies
            self.amount = amount
            self.duration = duration
            self.bonus_type = bonus_type
            self.stackable = stackable
    
        def add_bonus(self, target=None, category=None, categories=None):
            if target:
                print(str(target))
                print(category)
                print(categories)
            else:
                print("empty")
    
    
    class AbilityScore(Attribute):
        def __init__(self, name=None):
            super().__init__(name=name)
            self.modifier = math.floor((self.total - 10) / 2)
    
        @staticmethod
        def add_bonus(self, args=None):
            if args:
                for arg in args:
                    print(arg)
    
    
    class AbilityScores(Enum):
        STR = AbilityScore(name="Strength")
        DEX = AbilityScore(name="Dexterity")
        CON = AbilityScore(name="Constitution")
        INT = AbilityScore(name="Intelligence")
        WIS = AbilityScore(name="Wisdom")
        CHA = AbilityScore(name="Charisma")
        EMPTY = AbilityScore(name="EMPTY")
    
    
    class Bonuses:
        RACIAL = Bonus(bonus_type="racial")
        SIZE = Bonus(bonus_type="size")
        UNTYPED = Bonus(bonus_type="untyped", stackable=True)
        DODGE = Bonus(bonus_type="dodge", stackable=True)
    
    
    class Skill(Attribute):
        def __init__(self, name=None, ability=None):
            super(Attribute).__init__(name, ability)
            self.ranks = [0]
            self.class_skill = False
            self.armor_check = False
            self.trained_only = False
            self.base = self.ability.modifier
    
    
    class Skills(Enum):
        PERCEPTION = Skill(name="Perception", ability=AbilityScores.WIS)
        EMPTY = Skill(name="EMPTY", ability=AbilityScores.EMPTY)
        ALL = "all"
    
    
    class Sizes(Enum):
        SMALL = {
            "name": "small",
            "bonuses": [
                Bonuses.SIZE.add_bonus(amount=1, categories=["AC", "ATK_MELEE", "ATK_RANGED"]),
                Bonuses.SIZE.add_bonus(amount=-1, categories=["CMB", "CMD"]),
                Bonuses.SIZE.add_bonus(amount=4, category="Skill|Stealth")
            ]
        }
    
    
    class Specials(Enum):
        DEFENSE = "Special Defense"
        ATTACK = "Special Attack"
        ALL = "Special Defense"
    
    
    class ArmorClass(Attribute):
        def __init__(self, name="Armor Class", base=10):
            super(ArmorClass, self).__init__(name, base)
            self.flat = base
            self.touch = base
            self.total = base
            self.conditionals = []
            self.bonuses = {
                "ability modifier": AbilityScores.DEX.mod,
                "armor": 0,
                "dodge": 0,
                "shield": 0,
                "size": 0
            }
    
        @property
        def update_total(self):
            return -1
    
    
    class Attributes(Enum):
        INIT = Attribute(name="Initiative", ability=AbilityScores.DEX, base=AbilityScores.DEX.mod)
        AC = ArmorClass(name="Armor Class", ability=AbilityScores.DEX, base=AbilityScores.DEX.mod)
    
    
    class Saves(Enum):
        GOOD = "class_level / 2 + 2"
        POOR = "class_level / 3"
    
    
    class BaseClass:
        def __init__(self, name=None, hit_die=None, skill_pts=None, saves=[Saves.POOR, Saves.POOR, Saves.POOR],
                     class_skills=None,
                     base_attack=None,
                     level_progression=None, max_level=20):
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
    
    
    class CLASSES(Enum):
        FIGHTER = BaseClass(name="Fighter", hit_die=10, skill_pts=2, saves=[Saves.GOOD, Saves.POOR, Saves.POOR])
    
    
    class Race:
        pass
    
    
    class Gnome(Race):
        def __init__(self):
            self.name = "gnome"
            self.size = "Sizes.SMALL"
            self.race_type = "humanoid"
            self.race_subtype = "gnome"
            self.auto_lang = ["Lang.COMMON", "Lang.GNOME", "Lang.SYLVAN"]
            self.senses = ["low-light vision"]
            self.speed_base = 20
            self.bonuses = {
                "ability score": [
                    Bonuses.RACIAL.add_bonus(modifies=AbilityScores.STR, amount=-2, ),
                    Bonuses.RACIAL.add_bonus(modifies=AbilityScores.CON, amount=2),
                    Bonuses.RACIAL.add_bonus(modifies=AbilityScores.CHA, amount=2)]
            }
            self.racial_traits = {
                "Keen Senses": Bonuses.RACIAL,
                "Obsessive": Bonuses.RACIAL,
                "Illusion Resistance": Bonuses.RACIAL,
                "Hatred": Bonuses.UNTYPED,
                "Defensive Training": Bonuses.DODGE
            }
    
    
    class RACES(Enum):
    GNOME = Race(name="gnome")

"""

