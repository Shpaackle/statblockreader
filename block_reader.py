"""import os
import re
import pprint"""
import json
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s")
logging.debug("Start of program")

# list of common races and classes
races = ["gnome", "human", "elf", "half-elf", "half elf", "half-orc",
         "half orc", "dwarf", "halfling", "strix", "race"]
classes = ["sorcerer", "wizard", "cleric", "fighter",
           "rogue", "bard", "druid", "barbarian", "monk", "alchemist",
           "class"]

# Load different statblocks to test features
# statblock = open('./data/CustomStatBlock.txt')
# statblock = open('./data/ezren.txt')
# statblock = open('./data/acid_terror.txt')
statblock = open('./data/storm_prophet.txt')
# statblock = open('./data/mithral_wizard.txt')

# grab all lines of statblock
lines = statblock.readlines()

# split statblock by 'section'
sections = {
    "START": [],
    "DEFENSE": [],
    "OFFENSE": [],
    "STATISTICS": [],
    "SPECIAL ABILITIES": [],
    "TACTICS": []
}

# variable for current section
current = "START"

# iterate through every line in statblock
for line in lines:
    """ 
    if line is one of the keys, change which section to assign line to
    otherwise, add line to current section
    """
    if line.strip() in sections.keys():
        current = line.strip()
    else:
        sections[current].append(line)

# assign first line to key "name"
creature = {"name": sections["START"][0]}
# TODO use regex to grab CR from first line
"""
    check for CR in name line
    if found, assign to "cr" key
"""
if "CR" in creature["name"]:
    temp = creature["name"].split('CR')
    creature["name"] = temp[0].strip().title()
    creature["CR"] = temp[1].strip()
else:
    creature["name"] = creature["name"].strip().title()

# check for XP line, if not present quit
if "XP" not in sections["START"][1]:
    print("No XP line")
    quit(-1)
else:
    creature["XP"] = lines[1].split('XP')[1].strip()

# split gender/age/race/class line
temp = sections["START"][2].split()
for index in range(len(temp)):
    # strip word and convert to lowercase
    item = temp[index].strip().lower()
    """
    check if class section has been reached
    join previous word with the remaining words in list
    assign this to the "super_race" and break from loop
    """
    if item in classes:
        creature["super_race"] = " ".join(temp[index-1:])
        break
    # if word is gender, assign to "gender" key
    elif item in ["male", "female", "gender"]:
        creature["gender"] = item
    # if word is in age category list, assign to "age" key
    elif item in ["old", "middle-aged", "middle aged", "middle-age", "middle age", "young", "venerable", "age"]:
        creature["age"] = item

# split off first word in "super_race"
temp = creature["super_race"].split(" ", maxsplit=1)
"""
# if word is in races list assign this word to "race" key,
# everything else in "classes"
"""
if temp[0].lower() in races:
    creature["race"] = temp[0]
    creature["classes"] = temp[1]

# TODO use regex to parse classes more
temp = creature["classes"]
if "(" or "/" in temp:
    # archetype pass
    # multi-class pass
    logging.debug("Need to process classes more")

# split alignment/size/type line
temp = sections["START"][3].split()
# assign first item to alignment
creature["alignment"] = temp[0]
# assign second item to size
creature["size"] = temp[1]
# assign third item to type
creature["type"] = temp[2]
# check for subtype and assign if exists
if '(' in temp[-1]:
    length = len(temp[-1]) - 1
    creature["subtype"] = temp[-1][1:length]

# split initiative/senses line by ';' only once
temp = sections["START"][4].split(';', 1)
# split first item and assign last item in list to "init" key
creature["init"] = temp[0].split()[-1]
# split next item and assign last item in list to "senses" key
creature["senses"] = temp[1].strip().split(' ', 1)[-1]
# split and assign last item (should be +/- and integer) in list to "perception"
creature["perception"] = temp[1].split()[-1].strip()

# DEFENSE

# iterate through lines in "DEFEnSE" section
for line in sections["DEFENSE"]:
    # check first part of line
    if line[:2] == "AC":
        # assign line to "ac" key if first two letters are "AC"
        creature["ac"] = line.strip()
    elif line[:2].lower() == "hp":
        # assign line to "hp" key if first two letters are "hp"
        creature["hp"] = line.strip()
    elif "fort" in line.lower():
        # TODO increase sensitivity
        # split line by ';' if "fort" found in line
        semi = line.split(';')
        # iterate through items in list by index
        for index in range(len(semi)):
            # check index number
            if index == 0:
                # split first item in line by ','
                saves = semi[index].split(',')
                # iterate through list and apply to proper key
                for save in saves:
                    if save.split()[0].lower() == "fort":
                        creature["fort"] = save[5:]
                    elif save.split()[0].lower() == "ref":
                        creature["ref"] = save[4:].strip()
                    elif save.split()[0].lower() == "will":
                        creature["will"] = save[5:]
            elif "resist" in semi[index].split()[0].lower():
                # if statblock has resistances, apply to proper key
                creature["resist"] = semi[index].strip().split(' ', 1)[1]
            else:
                # if there are special properties for saves, apply to proper key
                creature["saves_special"] = semi[index].strip()
    elif "defensive" in line.split()[0].lower():
        # check for defensive abilities and apply to proper key
        creature["defensive_abilities"] = line.strip().split(' ', 2)[2]

# OFFENSE

# iterate through OFFENSE section by removing first line until len is 0
while len(sections["OFFENSE"]) > 0:
    # pop first line from 'OFFENSE'
    line = sections["OFFENSE"].pop(0).strip()
    # split line 
    test = line.split()
    # if first item is Speed
    if "Speed" in test[0]:
        # assign to 'speed' key
        creature["speed"] = test[1].strip()
    # if first item is Melee
    elif "Melee" in test[0]:
        # assign to 'melee' key
        creature["melee"] = " ".join(test[1:])
    # if first item is Ranged
    elif "Ranged" in test[0]:
        # join line after first item and assign to 'ranged' key
        creature["ranged"] = " ".join(test[1:])
    # join first two items and if this is Special Attack
    elif "Special Attack" in " ".join(test[0:2]):
        # join line after second item and assign to 'special_attacks' key
        creature["special_attacks"] = " ".join(test[2:])
    # if Spell-Like in the first three items, begin processing spell-like abilities
    elif "Spell-Like" in test[0:3]:
        # assign first line of spell-like block to new temporary dictionary under 'type' key
        sla = {"type": line.strip()}
        # iterate through remaining lines in 'OFFENSE'
        for item in sections["OFFENSE"]:
            # if item contains double dash 
            if "—" in item:
                # split by dash, assign first section to perday, second to abils
                perday, abils = item.split('—', 1)
                # check if perday contains either 'at will' or '/day'
                if "at will" in perday or "/day" in perday:
                    # assign abils to 'perday' key
                    sla[perday] = abils.strip()
                else:
                    # log error and break from loop
                    logging.debug("Couldn't find valid spell-like abilities")
                    break
        # assign dictionary to 'spell-like abilities' key
        creature["spell-like abilities"] = sla
    # if 'Spells' in first 3 words of line
    elif "Spells" in test[0:3]:
        # assign first line of spells to new temporary dictionary under 'type' key
        spells = {"type": line.strip()}
        # iterate through remaining lines in 'OFFENSE'
        for item in sections["OFFENSE"]:
            # if first character in line is a digit
            if item[0].isdigit():
                # split by double dash, assign first section to level, second to names
                level, names = item.split('—', 1)
                # assign names to 'level' key
                spells[level] = names.strip()
        # assign dictionary to 'spells' key
        creature["spells"] = spells
    # check for special notes at end of spell section, i.e. Opposition schools, domains, etc
    elif len(sections["OFFENSE"]) == 0:
        temp = line.split(' ')
        if "Opposition" in temp:
            special = [" ".join(temp[0:2]), " ".join(temp[2:])]
        else:
            special = [temp[0], " ".join(temp[1:])]
        creature[special[0]] = special[1]

# TACTICS
if sections["TACTICS"]:
    tactics = {}
    for line in sections["TACTICS"]:
        temp = line.split(' ', 2)
        tactics[" ".join(temp[0:2])] = temp[2]
    creature["tactics"] = tactics

# STATISTICS
while len(sections["STATISTICS"]) > 0:
    line = sections["STATISTICS"].pop(0)
    if "Str" in line.split()[0]:
        stats = line.split(',')
        for stat in stats:
            temp = stat.strip().split()
            creature[temp[0]] = temp[1]
    elif "Base" in line.split()[0]:
        temp = line.strip().split(';')
        creature["base_attack"] = temp[0].split()[-1]
        creature["cmb"] = temp[1].strip().split(" ", 1)[-1]
        creature["cmd"] = temp[2].strip().split(" ", 1)[-1]
    elif "Feats" in line.split()[0]:
        temp = line.strip().split(" ", 1)
        feats = temp[1].split(', ')
        creature["feats"] = feats
    elif "Skills" in line.split()[0]:
        temp = line.strip().split(" ", 1)
        skills = temp[1].split(', ')
        creature["skills"] = skills
    elif "Languages" in line.split()[0]:
        temp = line.strip().split(" ", 1)
        languages = temp[-1].split(', ')
        creature["languages"] = languages
    elif "SQ" in line.split()[0]:
        temp = line.strip().split(" ", 1)
        SQ = temp[-1].split(', ')
        creature["sq"] = SQ
    elif "Combat" in line.split()[0]:
        temp = line.split(" ", 2)
        gear = temp[-1].split(';')
        combat_gear = gear[0].split(', ')
        other_temp = gear[1].strip().split(" ", 2)
        other_gear = other_temp[-1].split(', ')
        creature["combat gear"] = combat_gear
        creature["other gear"] = other_gear

print(json.dumps(creature))
file_name = creature["name"].strip().split()
with open("_".join(file_name).lower()+".json","w") as file:
    json.dump(creature, file)
