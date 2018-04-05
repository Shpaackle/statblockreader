import json

from block_functions.creature import Creature


def main():
    file_name = "daring_bravo.json"
    with open(file_name) as f:
        block = json.load(f)

    character = Creature()
    character.stat_block = block

    print(len(character.stat_block))

	creature.assign_race()


if __name__ == '__main__':
    main()
