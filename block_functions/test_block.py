import json

from creature import Creature


def main():
    file_name = "daring_bravo.json"
    with open(file_name) as f:
        block = json.load(f)

    character = Creature()
    character.stat_block = block

    print(len(block))


if __name__ == '__main__':
    main()
