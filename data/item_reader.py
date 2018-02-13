import json
import logging
import pymongo

# logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s -  %(levelname)s -  %(message)s")
logging.debug("Start of program")


def database_connect():
    return pymongo.MongoClient(
        "mongodb://shpaackle:!d071379s$Boxy@itemdb-shard-00-00-wclgk.mongodb.net:27017,"
        "itemdb-shard-00-01-wclgk.mongodb.net:27017,"
        "itemdb-shard-00-02-wclgk.mongodb.net:27017/test?ssl=true&replicaSet=ItemDB-shard-0&authSource=admin")


def main():
    client = database_connect()
    db = client['ItemDB']

    with open('equipment.json') as file:
        equipment = json.load(file)

        armors = [e for e in equipment if "armor" in e.get("subcategory", "")]
        weapons = [e for e in equipment if e["family"] == "Weapons"]
        shields = [e for e in equipment if e.get("subcategory", "") == "Shields"]
        extras = [e for e in equipment if e.get("subcategory", "") == "Extras"]
        items = [e for e in equipment if e["category"] == "Item"]

    """
    armor_collection = db.armors
    armor_collection.add_many(armors)
    weapon_collection = db.weapons
    weapon_collection.add_many(weapons)
    shield_collection = db.shields
    shield_collection.add_many(shields)
    extras_collection = db.extras
    extras_collection.add_many(extras)
    items_collection = db.items
    items_collection.add_many(items)
    
    mi_json = "magic_items_"
    
"""
    print(armors[0]["name"])
    print(weapons[1]["name"])
    print(shields[-1]["name"])
    print(extras[0]["name"])
    print(items[10]["name"])


if __name__ == "__main__":
    main()

