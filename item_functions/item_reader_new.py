import json
import os
import logging as LOG
import pprint


def process_weapons(weapon):
    key_dict = {
        "body": "description",
        "name": "name",
        "weight": "weight",
        "price": "price",
        "source": "source",
        "Weapon Class": "subcategory",
        "Proficiency": "proficiency",
        "Range": "range",
        "Critical": "crit",
        "Type": "type",
        "Special": "special",
        "Dmg (T)": "dmg(T)",
        "Dmg (S)": "dmg(S)",
        "Dmg (M)": "dmg(M)",
        "Dmg (L)": "dmg(L)",
    }

    new_dict = {}
    misc = weapon.pop("misc", None)

    for k, v in key_dict.items():
        if misc["Weapon"].get(k, None):
            new_dict[v] = misc["Weapon"][k]
        elif weapon.get(k, None):
            new_dict[v] = weapon[k]

    return "weapons", new_dict


def process_armors(armor):
    """{
    "body": "<p>This small metal shield is worn strapped to your forearm. You can use a bow or crossbow without penalty while carrying it. You can also use your shield arm to wield a weapon (whether you are using an off-hand weapon or using your off hand to help wield a two-handed weapon), but you take a &ndash;1 penalty on attack rolls while doing so. This penalty stacks with those that may apply for fighting with your off hand and for fighting with two weapons. In any case, if you use a weapon in your off hand, you lose the buckler's AC bonus until your next turn. You can cast a spell with somatic components using your shield arm, but you lose the buckler's AC bonus until your next turn. You can't make a shield bash with a buckler.</p>", 
    "name": "Buckler", 
    "weight": "5 lbs.", 
    "url": "pfsrd://Core Rulebook/Rules/Equipment/Armor/Armor Descriptions/Buckler", 
    "price": "5 gp", 
    "misc": {
        "Armor": {
            "Armor Check Penalty": "&ndash;1", 
            "Maximum Dex Bonus": "&mdash;", 
            "Shield Bonus": "+1", 
            "Arcane Spell Failure Chance": "5%", 
            "Armor Type": "Shields", 
            "Speed (20 ft.)": "&mdash;", 
            "Speed (30 ft.)": "&mdash;"
        }
    }, 
    "source": "Core Rulebook", 
    "type": "item"
    }"""
    key_dict = {
        "body": "description",
        "name": "name",
        "weight": "weight",
        "price": "price",
        "source": "source",
        "Armor Check Penalty": "armor_check_penalty",
        "Maximum Dex Bonus": "maximum_dex_bonus",
        "Shield Bonus": "shield_bonus",
        "Armor Bonus": "armor_bonus",
        "Arcane Spell Failure Chance": "arcane_spell_failure_chance",
        "Armor Type": "armor_type",
        "Speed (20 ft.)": "speed_20",
        "Speed (30 ft.)": "speed_30",
        "Special": "special",
    }
    """{
    "body": "<p>Covering only the torso, a breastplate is made up of a single piece of sculpted metal.</p>", 
    "name": "Breastplate", 
    "weight": "30 lbs.", 
    "url": "pfsrd://Core Rulebook/Rules/Equipment/Armor/Armor Descriptions/Breastplate", 
    "price": "200 gp", 
    "misc": {
        "Armor": {
            "Armor Check Penalty": "&ndash;4", 
            "Maximum Dex Bonus": "+3", 
            "Arcane Spell Failure Chance": "25%", 
            "Armor Type": "Medium armor", 
            "Armor Bonus": "+6", 
            "Speed (20 ft.)": "15 ft.", 
            "Speed (30 ft.)": "20 ft."
        }
    }, 
    "source": "Core Rulebook", 
    "type": "item"
    }"""

    new_dict = {}
    misc = armor.pop("misc", None)

    for k, v in key_dict.items():
        if misc["Armor"].get(k, None):
            new_dict[v] = misc["Armor"][k]
        elif armor.get(k, None):
            new_dict[v] = armor[k]

    return "armors", new_dict


def process_magic_items(magic_item):
    """{
    "slot": "headband", -
    "name": "Headband of Alluring Charisma",-
    "weight": "1 lb.", -
    "cl": "8th", -
    "url": "pfsrd://Core Rulebook/Rules/Magic Items/Wondrous Items/Headband of Alluring Charisma", 
    "type": "item", 
    "price": "4,000 gp (+2), 16,000 gp (+4), 36,000 gp (+6)", -
    "misc": {
        "Construction": {-
            "Cost": "2,000 gp (+2), 8,000 gp (+4), 18,000 gp (+6)", 
            "Requirements": "Craft Wondrous Item, eagle's splendor"
        }
    }, 
    "source": "Core Rulebook", -
    "aura": "moderate transmutation", -
    "subtype": "headband", -
    "sections": [
        {
            "body": "<p>This attractive silver headband is decorated with a number of small red and orange gemstones. The headband grants the wearer an enhancement bonus to Charisma of +2, +4, or +6. Treat this as a temporary ability bonus for the first 24 hours the headband is worn.</p>", 
            "source": "Core Rulebook", 
            "type": "section", 
            "name": "Description"
        }
    ]
    }"""
    key_dict = {
        "body": "description",
        "name": "name",
        "weight": "weight",
        "price": "price",
        "source": "source",
        "slot": "slot",
        "subtype": "subtype",
        "Construction": "construction",
        "sections": "sections",
        "aura": "aura",
        "cl": "cl",
    }
    """{
    "slot": "none", 
    "name": "Apparatus of the Crab", 
    "weight": "500 lbs.", 
    "cl": "19th", 
    "url": "pfsrd://Core Rulebook/Rules/Magic Items/Wondrous Items/Apparatus of the Crab", 
    "type": "item", 
    "price": "90,000 gp", 
    "misc": {
        "Construction": {
            "Cost": "45,000 gp", 
            "Requirements": "Craft Wondrous Item, animate objects, continual flame, creator must have 8 ranks in Knowledge (engineering)"
        }
    }, 
    "source": "Core Rulebook", 
    "aura": "strong evocation and transmutation", 
    "sections": [
        {
            "body": "<p>At first glance, an inactive <i>apparatus of the crab</i> appears to be a large, sealed iron barrel big enough to hold two Medium creatures. Close examination, and a DC 20 Perception check, reveals a secret catch that opens a hatch at one end. Anyone who crawls inside finds 10 (unlabeled) levers and seating for two Medium or Small occupants. These levers allow those inside to activate and control the apparatus's movements and actions.</p>", 
            "type": "section", 
            "sections": [
                {
                    "body": "<table><thead><tr><th>Lever (1d10)</th><th>Lever Function</th></tr></thead><tbody><tr class=\"odd\"><td>1</td><td>Extend/retract legs and tail</td></tr><tr class=\"even\"><td>2</td><td>Uncover/cover forward porthole</td></tr><tr class=\"odd\"><td>3</td><td>Uncover/cover side portholes</td></tr><tr class=\"even\"><td>4</td><td>Extend/retract pincers and feelers</td></tr><tr class=\"odd\"><td>5</td><td>Snap pincers</td></tr><tr class=\"even\"><td>6</td><td>Move forward/backward</td></tr><tr class=\"odd\"><td>7</td><td>Turn left/right</td></tr><tr class=\"even\"><td>8</td><td>Open/close &ldquo;eyes&rdquo; with <i>continual flame </i>inside</td></tr><tr class=\"odd\"><td>9</td><td>Rise/sink in water</td></tr><tr class=\"even\"><td>10</td><td>Open/close hatch</td></tr></tbody></table>", 
                    "name": "Lever", 
                    "url": "pfsrd://Core Rulebook/Rules/Magic Items/Wondrous Items/Apparatus of the Crab/Description/Lever", 
                    "source": "Core Rulebook", 
                    "abbrev": "1d10", 
                    "type": "table"
                }, 
                {
                    "body": "<p>Operating a lever is a full-round action, and no lever may be operated more than once per round. However, since two characters can fit inside, the apparatus can move and attack in the same round. The device can function in water up to 900 feet deep. It holds enough air for a crew of two to survive 1d4+1 hours (twice as long for a single occupant). When activated, the apparatus looks something like a giant lobster.</p><p>When active, an <i>apparatus of the crab</i> has the following characteristics: <b>hp</b> 200; <b>hardness</b> 15; <b>Spd</b> 20 ft., swim 20 ft.; <b>AC</b> 20 (&ndash;1 size, +11 natural); <b>Attack</b> 2 pincers +12 melee (2d8); <b>CMB </b>+14; <b>CMD</b> 24.</p>", 
                    "source": "Core Rulebook", 
                    "type": "section"
                }
            ], 
            "name": "Description", 
            "source": "Core Rulebook"
        }
    ]
}"""

    new_dict = {}
    misc = magic_item.pop("misc", {})
    sections = magic_item.pop("sections", None)

    for k, v in key_dict.items():
        if misc.get(k, None):
            new_dict[v] = misc[k]
        elif magic_item.get(k, None):
            new_dict[v] = magic_item[k]

    for section in sections:
        if section.get("name", False) == "Description":
            new_dict["description"] = section["body"]

    return "magic_items", new_dict


def process_items(item):
    """{
    "body": "<p>This outfit includes a shirt with buttons, a skirt or pants with a drawstring, shoes, and perhaps a cap or hat. It may also include a belt or a leather or cloth apron for carrying tools.</p>", 
    "name": "Artisan's Outfit", 
    "weight": "4 lbs.1", 
    "url": "pfsrd://Core Rulebook/Rules/Equipment/Goods And Services/Clothing/Artisans Outfit", 
    "price": "1 gp", 
    "misc": {
        "null": {
            "Gear Type": "Clothing"
        }
    }, 
    "source": "Core Rulebook", 
    "type": "item"
    }"""
    key_dict = {
        "body": "description",
        "name": "name",
        "weight": "weight",
        "price": "price",
        "source": "source",
        "slot": "slot",
        "subtype": "subtype",
        "Construction": "construction",
        "sections": "sections",
        "aura": "aura",
        "cl": "cl",
        "Gear Type": "gear_type",
        "Craft": "craft",

    }
    """{
    "body": "<p>This leather knapsack has one large pocket that closes with a buckled strap and holds about 2 cubic feet of material. Some may have one or more smaller pockets on the sides. </p>", 
    "name": "Backpack", 
    "weight": "2 lbs.1", 
    "url": "pfsrd://Core Rulebook/Rules/Equipment/Goods And Services/Adventuring Gear/Backpack", 
    "price": "2 gp", 
    "misc": {
        "null": {
            "Gear Type": "Adventuring Gear"
        }
    }, 
    "source": "Core Rulebook", 
    "type": "item"
    }"""

    new_dict = {}
    misc = item.pop("misc", {})
    sections = item.pop("sections", None)

    for k, v in key_dict.items():
        if misc.get("null", False):
            if misc["null"].get(k, None):
                new_dict[v] = misc[k]
        elif item.get(k, None):
            new_dict[v] = item[k]

    for section in sections:
        if section.get("name", False) == "Description":
            new_dict["description"] = section["body"]
    return "general_items", item


def sort_item(item):
    misc = item.get("misc", {})

    if misc.get("Weapon", None):
        return process_weapons(item)
    elif misc.get("Armor", None):
        return process_armors(item)
    elif item.get("cl", r"&mdash") != r"&mdash":
        return process_magic_items(item)
    elif misc.get("null", False) or item.get("cl", False) or item.get("subtype", False):
        return process_items(item)
    else:
        return "manual", item


def get_files(top_folder):
    file_list = []
    for folder_path, sub_folders, files in os.walk(top_folder):
        for file in files:
            file_list.append(os.path.join(folder_path, file))

    return [x for x in file_list if os.path.splitext(x)[1] == ".json"]


def save_files(files):
    return files


def main():
    LOG.basicConfig(level=LOG.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s")
    LOG.debug("Start of program")

    item_folder = "./item/"
    # files = os.listdir(item_folder)

    # open all json files to be processed and add to json_list
    # json_list = [x for x in files if os.path.splitext(x)[1] == ".json"]
    json_list = get_files(item_folder)
    pprint.pprint(json_list[0:10])

    big_dict = {"weapons": [], "general_items": [], "manual": [], "magic_items": [], "armors": []}
    item_list = []

    for file in json_list:
        with open(file) as f:
            item = json.load(f)

        item_list.append(sort_item(item))

    for thing in item_list:
        big_dict[thing[0]].append(thing[1])

    """
        misc = item.get("misc", {})

        if misc.get("Weapon", None):

            big_dict["weapons"].append(process_weapons(item))
        elif misc.get("Armor", None):
            big_dict["armors"].append(process_armors(item))
        elif misc.get("Construction", None):
            big_dict["magic_items"].append(process_magic_items(item))
        elif misc.get("null"):
            big_dict["items"].append(process_items(item))
        else:
            big_dict["manual"].append(item)
    """
    for key in big_dict.keys():
        with open(key + ".json", "w") as file:
            json.dump(big_dict[key], file, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
