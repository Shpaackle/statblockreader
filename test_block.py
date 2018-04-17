import json

from block_functions.character import Character


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

    print("Finished")


if __name__ == '__main__':
    main()
