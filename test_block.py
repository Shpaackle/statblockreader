import json
import pprint

# from block_functions.creature import Creature
from block_functions.character import Character


def main():
    file_name = "daring_bravo.json"
    with open(file_name) as f:
        block = json.load(f)

    character = Character(block=block)
    print(block["race"])
    character.assign_race(block["race"].upper())

    print(len(character.block))
    assert character.alignment == block["alignment"]
    pprint.pprint(f"race: {type(character.race)}")
    assert character.race.name == "gnome"
    print("Finished")


if __name__ == '__main__':
    main()
