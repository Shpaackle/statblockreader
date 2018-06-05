import json
# import pytest
import logging
from pprint import pprint

from block_functions.character import Character

LOG = logging.getLogger(__name__).addHandler(logging.NullHandler())


def main():
    file_name = "daring_bravo.json"
    with open(file_name) as f:
        block = json.load(f)

    character = Character(block=block)
    character.assign_race(block["race"].upper())

    assert character.alignment == block["alignment"]
    assert character.race.name == "gnome"
    assert character.saves["FORT"].total == 0
    assert character.skills["Acrobatics"].armor_check is True
    assert character.scores["STR"].base == 10
    assert character.HP.ability is character.scores["CON"]
    assert character.speed.block == 20
    assert character.AC.ability is character.scores["DEX"]

    # CLASSES

    pprint(character.bonuses)

    print("Finished")


if __name__ == '__main__':
    main()
