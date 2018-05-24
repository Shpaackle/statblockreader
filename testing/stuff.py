from testing.db import *
from testing.model import *
import json
import re
from collections import *


test_db = connect(host="mongodb://shpaackle:!d071379s$Boxy@itemdb-shard-00-00-wclgk.mongodb.net:27017,"
                  "itemdb-shard-00-01-wclgk.mongodb.net:27017,"
                  "itemdb-shard-00-02-wclgk.mongodb.net:27017/test?ssl=true&replicaSet=ItemDB-shard-0"
                  "&authSource=admin")

if test_db:
    pprint.pprint("Successful mongoengine connection")
else:
    pprint.pprint("Unsuccessful mongoengine connection")
db = connect_to_database()
items = db.items
skills = [
    {
        "name": "Acrobatics",
        "ability": "Dex",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Appraise",
        "ability": "Int",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Bluff",
        "ability": "Cha",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Climb",
        "ability": "Str",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Craft",
        "ability": "Int",
        "untrained": True,
        "armor_check": False,
        "subtype": True,
        "tag": "Skill"
    },
    {
        "name": "Diplomacy",
        "ability": "Cha",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Disable Device",
        "ability": "Dex",
        "untrained": False,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Disguise",
        "ability": "Cha",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Escape Artist",
        "ability": "Dex",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Fly",
        "ability": "Dex",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Handle Animal",
        "ability": "Cha",
        "untrained": False,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Heal",
        "ability": "Wis",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Intimidate",
        "ability": "Cha",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Knowledge",
        "ability": "Int",
        "untrained": True,
        "armor_check": False,
        "subtype": True,
        "tag": "Skill"
    },
    {
        "name": "Linguistics",
        "ability": "Int",
        "untrained": False,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Perception",
        "ability": "Wis",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Perform",
        "ability": "Cha",
        "untrained": True,
        "armor_check": False,
        "subtype": True,
        "tag": "Skill"
    },
    {
        "name": "Profession",
        "ability": "Wis",
        "untrained": True,
        "armor_check": False,
        "subtype": True,
        "tag": "Skill"
    },
    {
        "name": "Ride",
        "ability": "Dex",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Sense Motive",
        "ability": "Wis",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Sleight of Hand",
        "ability": "Dex",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Spellcraft",
        "ability": "Int",
        "untrained": False,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Stealth",
        "ability": "Dex",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Survival",
        "ability": "Wis",
        "untrained": True,
        "armor_check": False,
        "tag": "Skill"
    },
    {
        "name": "Swim",
        "ability": "Str",
        "untrained": True,
        "armor_check": True,
        "tag": "Skill"
    },
    {
        "name": "Use Magic Device",
        "ability": "Cha",
        "untrained": False,
        "armor_check": False,
        "tag": "Skill"
    },
]

# add_to_database(items, skills)
# pprint.pprint(items.find_one({"name": "Perform"}))

# db_skills = items.find({'ability': {'$exists': True}})
# pprint.pprint(db_skills.count())
# items.delete_many({'ability': {'$exists': True}})
# db_skills = [item for item in items.objects if item["ability"] in ["Str", "Dex", "Cha", "Int", "Wis", "Cha"]]

# pprint.pprint(db_skills.count())
# for skill in db_skills:
#     print(skill)

"""###Block:"""
text_files = ["cr_equip_magic_items.lst", "cr_classes.lst"]
test_lines = ["header",
              "###Block:Metamagic Rods",
              "# Equipment Name		Output Name					Type			Cost		Weight	Base Item for "
              "EQMOD	Modifier					Source Page",
              "Headband of Alluring Charisma +2											TYPE:Magic.Wondrous.Headband																									COST:4000	WT:1										SOURCEPAGE:p.516																																																																																																																																																																																BONUS:STAT|CHA|2|TYPE=Enhancement",
              "Pearl of Power(1st Level)                                                TYPE: Magic.Wondrous    COST: "
              "1000 WT: 0.02                EQMOD: USES_PER_DAY_1 | CHARGES[1]               SOURCEPAGE: p.525",
              "Potion of Fox's Cunning					TYPE:Magic.Potion.Consumable	COST:300	WT:0		SOURCEPAGE:p.477	SPROP:+4 enhancement bonus to Intelligence for 3 minutes																						TEMPBONUS:ANYPC|STAT|INT|4|TYPE=Enhancement",
              "Scroll (Summon Monster VIII/Divine)			OUTPUTNAME:Scroll (Summon Monster VIII)		TYPE:Magic.Scroll.Divine.Consumable	COST:3000	WT:0.01	SOURCEPAGE:p.490",
              "",
              ]
start_index = 5

regex_dict = {
    "item_name": r"(?P<item_name>^.[^\t]+)",
    "item_tags": r"(?P<item_tag>(?P<tag_key>[A-Z]+)(?:[:])(?P<tag_value>[^\t]+)(?:\s+))",
    "block_tags": r"(?:^[# ]+)?(?P<block_tags>([^\t]+)(?:\s|\t)+)",
    "block_name": r"(?:###.+: *)(?P<block>.+)"
}

with open("../data/pcgen/core_rulebook/cr_equip_magic_items.lst") as f:
    lines = f.readlines()

header = []
last_index = 0
for l in lines:
    if l[1] == '#':
        break
    else:
        last_index += 1
        header.append(l)
pprint.pprint("header = {}  {}".format(header, last_index))

temp_dict = None
blocks = []
lst_items = []
block_found = False
for index, line in enumerate(lines):
    if len(line) < 1:
        continue

    if index < last_index:
        pass
    elif line[0] == '#':  # block tag, block headers, item notes
        if line[1] == "#":
            blocks.append(temp_dict)
            block_found = True
            block_name = re.search(regex_dict["block_name"], line).group(1)
            temp_dict = {"block_name": block_name}
        elif block_found:
            block_tags = re.findall(regex_dict["block_tags"], line)
            temp_dict["block_tags"] = [tag[1] for tag in block_tags]
            temp_dict["items"] = []
            block_found = False
        else:
            # add line to last item's "note" key, create if not found
            # if no items in block yet, add to block notes
            ...
    else:
        name = re.search(regex_dict["item_name"], lines[index])
        # pprint.pprint("name = {}".format(name))
        tags = re.findall(regex_dict["item_tags"], lines[index])
        if name:
            temp_dict["items"].append({"name": name.group(1), "tags": [tag[0] for tag in tags]})

final_dict = {"header": header, "blocks": blocks}
with open("../data/test_stuff.json", "w") as file:
    json.dump(final_dict, file, indent=4, sort_keys=True)
# pprint.pprint(temp_dict)

for _line in lines[10:21]:
    #pprint.pprint(_line.split('\t'), compact=True)
    ...
    for word in _line.split('\t'):
        if not word:
            #print("Empty", end='\t')
            ...
        else:
            print(word.strip(), end='\t')
    print('\n')


def lst_reader():
    ...
