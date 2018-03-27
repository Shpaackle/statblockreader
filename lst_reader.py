import os
import re
import pprint
import json
import logging
from data import bag_of_dicts

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s")
logging.debug("Start of program")

regex_dict = bag_of_dicts.regex_dict


def process_lst(lines):
    header = []
    last_index = 0
    for l in lines:
        if l[1] == '#':
            break
        else:
            last_index += 1
            header.append(l)

    blocks = header
    temp_dict = {}
    lst_items = []
    block_found = False
    index = 0
    for line in lines:
        if len(line) < 1 or index < last_index:
            index += 1
        elif line[0] == '#':
            if line[1] == '#':
                blocks.append(temp_dict)
                block_found = True
                block_name = re.search(regex_dict["block_name"], line).group(1)
                temp_dict = {"block_name": block_name, "items": []}
            elif block_found:
                block_tags = re.findall(regex_dict["block_tags"], line)
                temp_dict["block_tags"] = [tag[1] for tag in block_tags]
                block_found = False
            else:
                # add line to last item's "note" key, create if not found
                # if no items in block yet, add to block notes, create if needed
                ...
        else:
            split_line = line.split('/t')
            name = re.search(regex_dict["item_name"], lines[index])
            tags = re.findall(regex_dict["item_tags"], lines[index])
            if name:
                temp_dict["items"].append({"name": name.group(1), "tags": [tag[0] for tag in tags]})

    return [block for block in blocks if block]


manual_dict = {
    "cr_classes": {
        "header": range(0, 3),
        "barbarian": range(4, 12),
        "ex-barbarian": range(13, 19),
        "bard": range(21, 59),
        "cleric": range(61, 103),
        "druid": range(105, 162),
        "fighter": range(164, 201),
        "monk": range(203, 218),
        "paladin": range(220, 270),
        "ex-paladin": range(271, 283),
        "ranger": range(284, 330),
        "rogue": range(333, 340),
        "sorcerer": range(342, 377),
        "wizard": range(379, 438),
        "arcane archer": range(440, 464),
        "arcane trickster": range(465, 492),
        "assassin": range(494, 512),
        "dragon disciple": range(514, 538),
        "duelist": range(540, 559),
        "eldritch knight": range(560, 581),
        "loremaster": range(583, 604),
        "mystic theurge": range(605, 625),
        "pathfinder chronicler": range(627, 642),
        "shadowdancer": range(644, 662),
        "adept": range(665, 701),
        "aristocrat": range(702, 710),
        "commoner": range(711, 717),
        "expert": range(718, 727),
        "warrior": range(728, 736)
    },
    "cr_domains": {
        "header": range(0, 9),
        "domain reqs": range(10, 46),
        "domain block": range(47, 83)
    },
    "cr_races": {
        "header": range(0, 3),
        "races": range(4, 12)
    },
    "cr_abilities_race": {
        "header": range(0, 3),
        "block": range(5, 20),
        "dwarf": [range(24, 34), range(76, 88)],
        "elf": [range(35, 40), range(89, 96)],
        "gnome": [range(41, 49), range(97, 117)],
        "half-elf": [range(50 - 56), range(119, 120), range(127, 128)],
        "half-orc": [range(57 - 60), range(129, 137)],
        "halfling": [range(63, 68), range(138, 145)],
        "human": [range(69, 71), range(146, 150)]
    },
    "cr_feats": {
        "header": range(0, 5),
        "general feats": range(6, 186),
        "leadership": range(187, 190),
        "power attack": range(191, 201),
        "arcane strike": range(204, 207),
        "mod feats sorc bloodline": range(208, 249),
        "improved familiar": range(250, 260)
    },
    "cr__stats": {
        "header": range(0, 1),
        "ft": range(2, 3),
        "strength": range(3, 4),
        "dexterity": range(4, 5),
        "constitution": range(5, 6),
        "intelligence": range(6, 7),
        "wisdom": range(7, 8),
        "charisma": range(8, 9)
    },
    "cr_abilities_class": {
        "favored class": range(60, 73),
        "NPC classes": range(74, 80),
        "favored class bonus": range(85, 89),
        "new class system": range(90, 119),
        "barbarian SLP": range(136, 151),
        "ex-barbarian SLP": range(152, 161),
        "monk SLP": range(162, 187),
        "rogue SLP": range(188, 197),
        "rage": range(205, 209),
        "barbarian abilities": range(210, 226),
        "barbarian archetype support": range(228, 246),
        "barbarian block": range(247, 259),
        "barbarian rage powers": range(261, 291),
        "bard abilities": range(293, 305),
        "bardic performance": range(306, 351),
        "cleric abilities": range(353, 362),
        "cleric channel energy": range(363, 369),
        "core domain abilities": range(370, 405),
        "core domain define & vars": range(406, 441),
        "domain powers": range(478, 546),
        "druid abilities": range(547, 561),
        "nature's bond": range(563, 567),
        "fighter": range(666, 806),
        "weapon training": range(808, 875),
        "monk": [range(876, 916), range(918, 1735)],
        "paladin": range(1136, 1200),
        "ranger": range(1201, 1400),
        "rogue": range(1402, 1476),
        "sorcerer": range(1477, 1926),
        "wizard": range(1927, 2062),
        "expert": range(2065, 2072),
        "other": range(2074, 2126),
        "weapon/armor proficiencies": range(2128, 2175),
        "class core skills": range(2176, 2187),
        "uncanny dodge": range(2189, 2201),
        "evasion": range(2202, 2207),
        "common class abilities": range(2208, 2219),
        "arcane archer abilities": range(2268, 2277),
        "arcane trickster": range(2278, 2288),
        "assassin special": range(2290, 2307),
        "dragon disciple class features": range(2308, 2325),
        "duelist": range(2332, 2352),
        "eldritch knight": range(2354, 2360),
        "loremaster lore abilities": range(2362, 2372),
        "loremaster secrets": range(2374, 2386),
        "mystic theurge": range(2388, 2392),
        "pathfinder chronicler": range(2394, 2409),
        "shadowdancer": range(2411, 2434)
    }
}


def manual_process(lines, file_dict):
    temp_dict = {}
    for k, v in manual_dict[file_dict].items():
        tags = []
        for index in v:
            logging.debug("v = " + str(v))
            try:
                tags.append([tag.lstrip('# ') for tag in lines[int(index)].strip().split('\t') if tag])
            except TypeError:
                for val in v:
                    for i in val:
                        tags.append([tag.lstrip('# ') for tag in lines[int(i)].strip().split('\t') if tag])

        temp_dict[k] = [tag for tag in tags if tag]

    if temp_dict:
        return temp_dict
    else:
        return -1


def main():
    data_folder = "./data/pcgen/core_rulebook"
    files = os.listdir(data_folder)
    lst_files = [x for x in files if os.path.splitext(x)[1] == ".lst"]
    logging.debug(lst_files)

    for file in lst_files:
        file_name = os.path.splitext(file)[0]
        logging.debug("file_name = {}".format(file_name))
        if file_name in manual_dict.keys():
            logging.debug("file ({}) found successfully".format(file_name))
            with open(os.path.join(data_folder, file)) as f:
                lines = f.readlines()
                logging.debug("length = {}".format(len(lines)))
            json_file = manual_process(lines, file_name)
            logging.debug("keys length = {}".format(len(json_file.keys())))
            with open("{0}/data_{1}.json".format(data_folder, file_name), 'w') as jf:
                logging.debug(str(jf))
                json.dump(json_file, jf, indent=4)


if __name__ == '__main__':
    main()
