'''Statblock parser'''

import os
import sys
import re
import json
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s")
logging.debug("Start of program")

# list of common races and classes
RACES = ["gnome", "human", "elf", "half-elf", "half elf", "half-orc",
         "half orc", "dwarf", "halfling", "strix", "race"]
CLASSES = ["sorcerer", "wizard", "cleric", "fighter",
           "rogue", "bard", "druid", "barbarian", "monk", "alchemist",
           "class"]

regex = {
    "spells" : re.compile("(?P<level>[0-9])(?:[a-z]{2})? ?(?P<perday>\([A-z0-9 /]+\))?[^A-z0-9]*(?P<spells>[A-z0-9(),'/ ]+)$"),
    "name_and_cr" : re.compile("(?P<name>[A-z0-9 ']+?)(?: CR )?(?P<cr>[0-9]+)?$"),
    "xp" : re.compile("XP (?P<xp>[0-9,]+)"),
    "gender_age_class" : re.compile("(?P<gender>Male|Female)? ?(?P<age>old|middle-aged|middle aged|middle-age|middle age|young|venerable|age)? ?(?P<race>[A-z]+) (?P<class>[A-z ]+) (?P<level>[0-9]+)(/?(?P<class2>[A-z ]+) (?P<level2>[0-9]+))?(/?(?P<class3>[A-z ]+) (?P<level3>[0-9]+))?"),
    "alignment_size_type_subtype" : re.compile("(?P<alignment>[A-z]+) (?P<size>[A-z]+) (?P<type>[A-z ]+) \((?P<subtype>[A-z -]+)\)"),
    "init_senses_perception" : re.compile("Init (?P<init>[+-0-9]+); Senses (?P<senses>[A-z0-9 .]);? Perception (?P<perception>[+-0-9]+)"),
    "defense" : re.compile("AC (?P<ac>[0-9]+), touch (?P<touch>[0-9]+), flat-footed (?P<flatfooted>[0-9]+) \((?P<ac_stat0>[0-9+-]+)? ?(?P<ac_component0>[A-z]+)?,? ?(?P<ac_stat1>[0-9+-]+)? ?(?P<ac_component1>[A-z]+)?,? ?(?P<ac_stat2>[0-9+-]+)? ?(?P<ac_component2>[A-z]+)?,? ?(?P<ac_stat3>[0-9+-]+)? ?(?P<ac_component3>[A-z]+)?,? ?(?P<ac_stat4>[0-9+-]+)? ?(?P<ac_component4>[A-z]+)?,? ?(?P<ac_stat5>[0-9+-]+)? ?(?P<ac_component5>[A-z]+)?,? ?(?P<ac_stat6>[0-9+-]+)? ?(?P<ac_component6>[A-z]+)?,? ?(?P<ac_stat7>[0-9+-]+)? ?(?P<ac_component7>[A-z]+)?\)"),
    "saves" : re.compile("Fort (?P<fortitude>[+-0-9]+), Ref (?P<reflex>[+-0-9]+), Will (?P<will>[+-0-9]+)(; )?(?P<save_modifiers>[^;]+)(; )?(?P<resists>.+)$"),
    "defensive_abilities" : re.compile("Defensive Abilities (?P<defensive_abilities>.+)"),
    "speed" : re.compile("Speed (?P<speed>[0-9]+) ft."),
    "caster_level" : re.compile("(?P<spell_class>[A-z]+) Spells (Known|Prepared) \(CL (?P<caster_level>[0-9]+..); concentration (?P<concentration>[+0-9]+)(, )?(arcane spell failure )?(?P<arcane_spell_failure>[0-9]+)?"),
    "ability_scores" : re.compile("Str (?P<strength>[0-9]+), Dex (?P<dexterity>[0-9]+), Con (?P<constitution>[0-9]+), Int (?P<Intelligence>[0-9]+), Wis (?P<wisdom>[0-9]+), Cha (?P<charisma>[0-9]+)"),
    "attacks" : re.compile("Base Atk (?P<base_attack>[-+0-9]+); CMB (?P<cmb>[-+0-9]+)( \((?P<cmb_extra>[-+0-9]+ [A-z ]+)\))?; CMD (?P<cmd>[0-9]+)( \((?P<cmd_extra>[-+0-9]+ [A-z. ]+)\))?"),
    "feats_skills_languages" : re.compile(" ([^,]+)"),

}

def main():
    data_folder = './data/'
    # Load different statblocks to test features
    # statblock = 'CustomStatBlock.txt'
    # statblock = 'ezren.txt'
    # statblock = 'acid_terror.txt'
    # statblock = 'storm_prophet.txt'
    # statblock = 'mithral_wizard.txt'
    files = os.listdir(data_folder)

    # grab all files that end in .txt
    statblocks = [x for x in files if os.path.splitext(x)[1] == ".txt"]

    # go through our grabbed files
    for statblock in statblocks:
        with open(os.path.join(data_folder, statblock)) as f:
            # grab all lines of statblock
            lines = f.readlines()

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
            stripped_line = line.strip()
            if stripped_line in sections:
                current = stripped_line
            else:
                sections[current].append(line)
        # create dict to hold data
        creature = {}

        try:
            if not sections["START"]:
                continue
            line = sections["START"][0]
            # Get name and CR   
            creature = match_line("name_and_cr", line, creature)

            line = sections["START"][1]
            # check for XP line, if not present quit
            creature = match_line("xp", line, creature)

            line = sections["START"][2]
            creature = match_line("gender_age_class", line, creature)

            # split gender/age/race/class line
        #    temp = sections["START"][2].split()
        #    for index in range(len(temp)):
                # strip word and convert to lowercase
        #        item = temp[index].strip().lower()
    #            check if class section has been reached
    #            join previous word with the remaining words in list
    #            assign this to the "super_race" and break from loop
        #        if item in CLASSES:
        #            creature["super_race"] = " ".join(temp[index-1:])
        #            break
                # if word is gender, assign to "gender" key
        #        elif item in ["male", "female", "gender"]:
        #            creature["gender"] = item
                # if word is in age category list, assign to "age" key
        #        elif item in ["old", "middle-aged", "middle aged", "middle-age", "middle age", "young", "venerable", "age"]:
        #            creature["age"] = item

            # split off first word in "super_race"
            #temp = creature["super_race"].split(" ", maxsplit=1)
            # if word is in races list assign this word to "race" key,
            # everything else in "classes"
            #if temp[0].lower() in RACES:
            #    creature["race"] = temp[0]
            #    creature["classes"] = temp[1]

            # TODO use regex to parse classes more
            #temp = creature["classes"]
            #if "(" or "/" in temp:
                # archetype pass
                # multi-class pass
            #    logging.debug("Need to process classes more")

            

            # split alignment/size/type line
            line = sections["START"][3]
            creature = match_line("alignment_size_type_subtype", line, creature)

            # assign first item to alignment
        #    creature["alignment"] = temp[0]
            # assign second item to size
        #    creature["size"] = temp[1]
            # assign third item to type
        #    creature["type"] = temp[2]
            # check for subtype and assign if exists
        #    if '(' in temp[-1]:
        #        length = len(temp[-1]) - 1
        #        creature["subtype"] = temp[-1][1:length]


            line = sections["START"][4]
            creature = match_line("init_senses_perception", line, creature)

            # split initiative/senses line by ';' only once
            #temp = sections["START"][4].split(';', 1)
            # split first item and assign last item in list to "init" key
            #creature["init"] = temp[0].split()[-1]
            # split next item and assign last item in list to "senses" key
            #creature["senses"] = temp[1].strip().split(' ', 1)[-1]
            # split and assign last item (should be +/- and integer) in list to "perception"
            #creature["perception"] = temp[1].split()[-1].strip()

            # DEFENSE
            line = sections["DEFENSE"][0]
            creature = match_line("defense", line, creature)

            line = sections["DEFENSE"][1]
            creature = match_line("saves", line, creature)

            if len(sections["DEFENSE"]) > 2:
                creature = match_line("defensive_abilities", line, creature)

            # iterate through lines in "DEFEnSE" section
        #    for line in sections["DEFENSE"]:
                # check first part of line
        #        if line[:2] == "AC":
                    # assign line to "ac" key if first two letters are "AC"
        #            creature["ac"] = line.strip()
        #        elif line[:2].lower() == "hp":
                    # assign line to "hp" key if first two letters are "hp"
        #            creature["hp"] = line.strip()
        #        elif "fort" in line.lower():
                    # TODO increase sensitivity
                    # split line by ';' if "fort" found in line
        #            semi = line.split(';')
                    # iterate through items in list by index
        #            for index in range(len(semi)):
                        # check index number
        #                if index == 0:
                            # split first item in line by ','
        #                    saves = semi[index].split(',')
                            # iterate through list and apply to proper key
        #                    for save in saves:
        #                        if save.split()[0].lower() == "fort":
        #                            creature["fort"] = save[5:]
        #                        elif save.split()[0].lower() == "ref":
        #                            creature["ref"] = save[4:].strip()
        #                        elif save.split()[0].lower() == "will":
        #                            creature["will"] = save[5:]
        #                elif "resist" in semi[index].split()[0].lower():
                            # if statblock has resistances, apply to proper key
        #                    creature["resist"] = semi[index].strip().split(' ', 1)[1]
        #                else:
                            # if there are special properties for saves, apply to proper key
        #                    creature["saves_special"] = semi[index].strip()
        #        elif "defensive" in line.split()[0].lower():
                    # check for defensive abilities and apply to proper key
        #            creature["defensive_abilities"] = line.strip().split(' ', 2)[2]

            # OFFENSE
            line = sections["OFFENSE"][0]
            creature = match_line("speed", line, creature)

            while sections["OFFENSE"]:
                line = sections["OFFENSE"].pop(0)
                temp = line.strip().split()
                if not temp:
                    continue
                if "Melee" in temp[0]:
                    creature["melee"] = " ".join(temp[1:])
                elif "Ranged" in temp[0]:
                    creature["ranged"] = " ".join(temp[1:])
                elif "Special Attack" in " ".join(temp[0:2]):
                    creature["special_attacks"] = " ".join(temp[2:])
                elif "Spell-Like" in temp[0:3]:
                    sla = {"type": line.strip()}
                    for item in sections["OFFENSE"]:
                        if "—" in item:
                            perday, abils = item.split('—', 1)
                            if "at will" in perday or "/day" in perday:
                                sla[perday] = abils.strip()
                            else:
                                break
                    creature["spell-like abilities"] = sla
                elif match_re("caster_level", line):
                    creature = match_line("caster_level", line, creature)
                    spells = {}
                    for item in sections["OFFENSE"]:
                        if item[0].isdigit():
                            #level, names = item.split('—', 1)
                            try:
                                match = regex["spells"].match(item)
                                d = match.groupdict()
                                spells[d["level"]] = d["spells"].strip()
                            except:
                                print(item)
                    creature["spells"] = spells
                elif not sections["OFFENSE"]:
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
                split_line = line.split(" ", 1)
                first = split_line[0]
                if len(split_line) > 1:
                    rest = split_line[1].strip()
                else:
                    rest = ""
                match_line("ability_scores", line, creature)
                match_line("attacks", line, creature)
#                if "Str" in line.split()[0]:
#                    stats = line.split(',')
#                    for stat in stats:
#                        temp = stat.strip().split()
#                        creature[temp[0]] = temp[1]
#                elif "Base" in line.split()[0]:
#                    temp = line.strip().split(';')
#                    creature["base_attack"] = temp[0].split()[-1]
#                    creature["cmb"] = temp[1].strip().split(" ", 1)[-1]
#                    creature["cmd"] = temp[2].strip().split(" ", 1)[-1]
                if "Feats" in first:
                    creature["feats"] = regex["feats_skills_languages"].findall(rest)
#                    temp = line.strip().split(" ", 1)
#                    feats = temp[1].split(', ')
#                    creature["feats"] = feats
                elif "Skills" in first:
                    creature["skills"] = regex["feats_skills_languages"].findall(rest)
#                    temp = line.strip().split(" ", 1)
#                    skills = temp[1].split(', ')
#                    creature["skills"] = skills
                elif "Languages" in first:
                    creature["languages"] = regex["feats_skills_languages"].findall(rest)
#                    temp = line.strip().split(" ", 1)
#                    languages = temp[-1].split(', ')
#                    creature["languages"] = languages
                elif "SQ" in first:
                     creature["sq"] = regex["feats_skills_languages"].findall(rest)
#                    temp = line.strip().split(" ", 1)
#                    SQ = temp[-1].split(', ')
#                    creature["sq"] = SQ
                elif "Combat" in first:
                    temp = line.split(" ", 2)
                    gear = temp[-1].split(';')
                    combat_gear = gear[0].split(', ')
                    other_temp = gear[1].strip().split(" ", 2)
                    other_gear = other_temp[-1].split(', ')
                    creature["combat gear"] = combat_gear
                    creature["other gear"] = other_gear

            #print(json.dumps(creature))
            file_name = creature["name"].strip().split()
            with open("_".join(file_name).lower()+".json","w") as file:
                json.dump(creature, file)

        except :
            print("Unexpected error:", sys.exc_info()[0])
            print("line: ", line)
            raise

def match_line(regex_name, line, creature):
    match = regex[regex_name].match(line)
    if match:
        for key in match.groupdict():
            creature[key] = match.groupdict()[key]
    return creature

def match_re(regex_name, line):
    return regex[regex_name].match(line)

if __name__ == "__main__":
    main()

