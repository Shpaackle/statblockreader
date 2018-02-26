import os
import json


from test.db import connect_to_database as connect_db


def get_block(file_name):
    """
    check if json file
    then open json and return file
    otherwise, return None
    """
    if os.path.splitext(file_name)[1] == ".json":
        file = open(file_name)
        return json.load(file)
    else:
        return None


def get_classes(block):
    classes = [(block["class"], block["level"]),
               (block.get("class2", None), block.get("level2", None)),
               (block.get("class3", None), block.get("level3", None))]

    return classes


def parse_classes(block_classes, character):
    pass


def parse_race(block_race, character):
    pass


def parse_skills(block_skills, character):
    pass


def parse_feats(block_feats, character):
    pass


def parse_equipment(block_gear, character):
    pass


def check_hp(block_hp, character):
    pass


def check_saves(block_saves, character):
    pass


def main():
    print("start")
    db = connect_db()
    items = db.items
    print(type(items))
    character = {}
    file_name = "../data/acid_terror.json"
    block = get_block(file_name)
    if not block:
        print("File did not load correctly")
        return -1
    parse_classes(get_classes(block), character)
    parse_race(block["race"], character)
    parse_skills(block["skills"], character)
    parse_feats(block["feats"], character)
    parse_equipment([block["combat gear"], block["other gear"]], character)

    check_hp(block, character)
    check_saves(block, character)


if __name__ == "__main__":
    main()
