from enum import Enum


classes = {
    "bard": {
        "hd": "d8",
        "starting_wealth": ("3d6", 10), 
        "alignment": [],
        "skills": [], # indices refer to list of skills
        "skill_pts": "6", 
        "BAB": "3/4",
        "saves": [(0, 2, 2)], 
        "spells/day": [[]], 
        "spells_known": [[]],
        "abilities": [[]]
    }
}

races = {
    "half-elf": {
        
    }
}


class Skills(Enum):
    Acrobatics = 0
    Appraise = 1
    Bluff = 2
    Climb = 3
    Craft = 4
    Diplomacy = 5
    Disable_Device = 6
    Disguise = 7
    Escape_Artist= 8
    Fly = 9
    Handle_Animal = 10
    Heal = 11
    Intimidate = 12
    arcana = 13
    dungeoneering = 14
    engineering = 15
    geography = 16
    history = 17
    local = 18
    nature = 19
    nobility = 20
    planes = 21
    religion = 22
    Linguistics = 23
    Perception = 24
    Profession = 25
    Ride = 26
    Sense_Motive = 27
    Sleight_of_Hand = 28
    Spellcraft = 29
    Stealth = 30
    Survival = 31
    Swim = 32
    Use_Magic_Device = 33


def check_skills(self, sb):
    # load skill list and pts data for classes of sb
    # sum total skill points sb should have by class and stats
    # split sb skills with regex 
    # remove ability modifiers from sb
    # check for class skills and remove from sb
    # check race vs skills
    # check gear vs skills
    # check feats vs skills
    pass


GOOD = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
POOR = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
big_dict = {
    "class skills": {
        "barbarian":    [1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0],
        "bard":         [1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1],
        "cleric":       [0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0],
        "druid":        [0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0],
        "fighter":      [0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0],
        "monk":         [1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0],
        "paladin":      [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0],
        "ranger":       [0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,1,1,1,1,0],
        "rogue":        [1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1],
        "sorcerer":     [0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
        "wizard":       [0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0]
    },
    "PointBuy": {
        "7": -4,
        "8": -2,
        "9": -1,
        "10": 0,
        "11": 1,
        "12": 2,
        "13": 3,
        "14": 5,
        "15": 7,
        "16": 10,
        "17": 13,
        "18": 17
    },
    "classes": {
        "bard": {
            "hd": "d8",
            "starting_wealth": ("3d6 x 10", 105),
            "alignment": [0, 0, 0, 0, 0, 0, 0, 0, 0],
            "skills": [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            "skill_pts": 6,
            "BAB": "3/4",
            "saves": [POOR, GOOD, GOOD],
            "spells/day": [[]],
            "spells_known": [[]],
            "abilities": [[]]
        }
    },
    "magic items": {
        "wondrous items": [
            {
                "name": "Headband of Alluring Charisma +2",
                "weight": "1",
                "slot": "ItemSlots.Headband",
                "price": "4,000",
                "cost": "2,000",
                "bonus": [("CHA", 2, "enhancement")],
                "group": "MagicItems.WondrousItem"
            },
            {
                "name": "Cloak of Resistance +1",
                "weight": "1",
                "slot": "ItemSlots.Back",
                "price": "2,000",
                "cost": "1,000",
                "bonus": [("Fort", 1, "resistance"), ("Ref", 1, "resistance"), ("Will", 1, "resistance")],
                "group": "MagicItems.WondrousItem"
            },
            {
                "name": "Ring of Protection +1",
                "weight": None,
                "slot": "ItemSlots.Ringer",
                "price": "2,000",
                "cost": "1,000",
                "bonus": [("AC", 1, "deflection")],
                "group": "MagicItems.Ring"
            },
            {
                "name": ""
            }
        ]
    }
}
