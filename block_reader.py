'''Statblock parser'''
import pprint
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

REGEX = {
    "spells" : re.compile("(?P<level>[0-9])(?:[a-z]{2})? ?(?P<perday>\([A-z0-9 /]+\))?[^A-z0-9]*(?P<spells>[A-z0-9(),'/ ]+)$"),
    "name_and_cr" : re.compile("(?P<name>[A-z0-9 ']+?)(?: CR )?(?P<cr>[0-9]+)?$"),
    "xp" : re.compile("XP (?P<xp>[0-9,]+)"),
    "gender_age_class" : re.compile("(?P<gender>Male|Female)? ?(?P<age>old|middle-aged|middle aged|middle-age|middle age|young|venerable|age)? ?(?P<race>[A-z]+) (?P<class>[A-z ]+) (?P<level>[0-9]+)(/?(?P<class2>[A-z ]+) (?P<level2>[0-9]+))?(/?(?P<class3>[A-z ]+) (?P<level3>[0-9]+))?"),
    "alignment_size_type_subtype" : re.compile("(?P<alignment>[A-z]+) (?P<size>[A-z]+) (?P<type>[A-z ]+) \((?P<subtype>[A-z -]+)\)"),
    "init_senses_perception" : re.compile("Init (?P<init>[-+0-9]+); Senses (?P<senses>[A-Za-z0-9. ]+)(;)? Perception ("
                                          "?P<perception>[-+0-9]+)"),
    "defense" : re.compile("AC (?P<ac>[0-9]+), touch (?P<touch>[0-9]+), flat-footed (?P<flatfooted>[0-9]+) \((?P<ac_stat0>[0-9+-]+)? ?(?P<ac_component0>[A-z]+)?,? ?(?P<ac_stat1>[0-9+-]+)? ?(?P<ac_component1>[A-z]+)?,? ?(?P<ac_stat2>[0-9+-]+)? ?(?P<ac_component2>[A-z]+)?,? ?(?P<ac_stat3>[0-9+-]+)? ?(?P<ac_component3>[A-z]+)?,? ?(?P<ac_stat4>[0-9+-]+)? ?(?P<ac_component4>[A-z]+)?,? ?(?P<ac_stat5>[0-9+-]+)? ?(?P<ac_component5>[A-z]+)?,? ?(?P<ac_stat6>[0-9+-]+)? ?(?P<ac_component6>[A-z]+)?,? ?(?P<ac_stat7>[0-9+-]+)? ?(?P<ac_component7>[A-z]+)?\)"),
    "hp" : re.compile("hp (?P<hp>[0-9]+) \((?P<hitdice>[0-9d+]+)\)"),
    "saves" : re.compile("Fort (?P<fortitude>[-+0-9]+), Ref (?P<reflex>[-+0-9]+), Will (?P<will>[-+0-9]+)(; )?("
                         "?P<save_modifiers>[^;]+)(; )?(?P<resists>.+)$"),
    "defensive_abilities" : re.compile("Defensive Abilities (?P<defensive_abilities>.+)"),
    "speed" : re.compile("Speed (?P<speed>[0-9]+) ft."),
    "caster_level" : re.compile("(?P<spell_class>[A-z]+) Spells (Known|Prepared) \(CL (?P<caster_level>[0-9]+..); concentration (?P<concentration>[+0-9]+)(, )?(arcane spell failure )?(?P<arcane_spell_failure>[0-9]+)?"),
    "ability_scores" : re.compile("Str (?P<strength>[0-9]+), Dex (?P<dexterity>[0-9]+), Con (?P<constitution>[0-9]+), Int (?P<Intelligence>[0-9]+), Wis (?P<wisdom>[0-9]+), Cha (?P<charisma>[0-9]+)"),
    "attacks" : re.compile("Base Atk (?P<base_attack>[-+0-9]+); CMB (?P<cmb>[-+0-9]+)( \((?P<cmb_extra>[-+0-9]+ [A-z ]+)\))?; CMD (?P<cmd>[0-9]+)( \((?P<cmd_extra>[-+0-9]+ [A-z. ]+)\))?"),
    "feats_skills_languages" : re.compile(r',\s*(?![^()]*\))'),  #(" ?([^,]+)")
    "melee" : re.compile("Melee (?P<melee>.+)"),
    "ranged" : re.compile("Ranged (?P<ranged>.+)"),
    "special_attacks" : re.compile("Special Attack (?P<special_attacks>.+)"),
    "spell-like_abilities" : re.compile("Spell-Like Abilities \(CL (?P<spell_like_cl>[0-9]+)..; concentration (?P<spell_like_concentration>[-+0-9]+)\)"),

}


def main():
    data_folder = './data/'
    # Load different statblocks to test features
    files = os.listdir(data_folder)

    # grab all files that end in .txt
    statblocks = [x for x in files if os.path.splitext(x)[1] == ".txt"]
    print(statblocks)
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
            line = sections["START"].pop(0)
            creature = match_line("name_and_cr", line, creature)
            line = sections["START"].pop(0)
            creature = match_line("xp", line, creature)
            for line in sections["START"]:
                # Get name and CR
                #creature = match_line("name_and_cr", line, creature)
                #creature = match_line("xp", line, creature)
                creature = match_line("gender_age_class", line, creature)

            # split alignment/size/type line
                creature = match_line("alignment_size_type_subtype", line, creature)
                creature = match_line("init_senses_perception", line, creature)

            # DEFENSE
            for line in sections["DEFENSE"]:
                creature = match_line("defense", line, creature)
                creature = match_line("hp", line, creature)
                creature = match_line("saves", line, creature)
                creature = match_line("defensive_abilities", line, creature)

            # OFFENSE          
            spells = {}
            for line in sections["OFFENSE"]:
                creature = match_line("speed", line, creature)
                temp = line.strip().split()
                if not temp:
                    continue
                creature = match_line("melee", line, creature)
                creature = match_line("ranged", line, creature)
                creature = match_line("special_attacks", line, creature)
                creature = match_line("spell-like_abilities", line, creature)
                creature = match_line("caster_level", line, creature)
                lvlspells = match_spells(line)
                if lvlspells:
                    spells[lvlspells["level"]] = {
                    "spells": lvlspells["spells"].strip().split(", "),
                    "perday": lvlspells["perday"]
                    }
            creature["spells"] = spells
#                if not sections["OFFENSE"]:
#                    temp = line.split(' ')
#                    if "Opposition" in temp:
#                        special = [" ".join(temp[0:2]), " ".join(temp[2:])]
#                    else:
#                        special = [temp[0], " ".join(temp[1:])]
#                    creature[special[0]] = special[1]

            # TACTICS
            if sections["TACTICS"]:
                tactics = {}
                for line in sections["TACTICS"]:
                    temp = line.split(' ', 2)
                    tactics[" ".join(temp[0:2])] = temp[2]
                creature["tactics"] = tactics

            # STATISTICS
            for line in sections["STATISTICS"]:
                split_line = line.split(" ", 1)
                first = split_line[0]

                if len(split_line) > 1:
                    rest = split_line[1].strip()
                else:
                    rest = ""

                match_line("ability_scores", line, creature)
                match_line("attacks", line, creature)
                
                if "Feats" in first:
                    creature["feats"] = REGEX["feats_skills_languages"].split(rest)
                elif "Skills" in first:
                    creature["skills"] = REGEX["feats_skills_languages"].split(rest)
                elif "Languages" in first:
                    creature["languages"] = REGEX["feats_skills_languages"].split(rest)
                elif "SQ" in first:
                     creature["sq"] = REGEX["feats_skills_languages"].split(rest)
                elif "Combat" in first:
                    temp = line.split(" ", 2)
                    gear = temp[-1].split(';')
                    combat_gear = gear[0].split(', ')
                    other_temp = gear[1].strip().split(" ", 2)
                    other_gear = other_temp[-1].split(', ')
                    creature["combat gear"] = combat_gear
                    creature["other gear"] = other_gear

            # print(json.dumps(creature))
            if "name" in creature:
                file_name = creature["name"].strip().split()
                with open(data_folder + "_".join(file_name).lower()+".json", "w") as file:
                    json.dump(creature, file, indent=4, sort_keys=True)

        except :
            print("Unexpected error:", sys.exc_info()[0])
            print("line: ", line)
            raise


def match_line(regex_name, line, creature):
    """Returns creature with matches from regex_name included as a new key/value pair
    """
    match = REGEX[regex_name].match(line)
    if match:
        for key in match.groupdict():
            if key not in creature:
                creature[key] = match.groupdict()[key]
    return creature


def match_re(regex_name, line):
    """Returns True if line matches regex_name
    """
    return REGEX[regex_name].match(line)


def match_spells(line):
    """extract spells from line
    """
    spells = {}
    match = REGEX["spells"].match(line)
    if match:
        for key in match.groupdict():
            spells[key] = match.groupdict()[key]
    return spells
    

if __name__ == "__main__":
    main()

    logging.debug("End of program")
