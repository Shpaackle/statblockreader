import pymongo
import json
import pprint


def connect_to_database():
    client = pymongo.MongoClient(
        "mongodb://shpaackle:!d071379s$Boxy@itemdb-shard-00-00-wclgk.mongodb.net:27017,itemdb-shard-00-01-wclgk.mongodb.net:27017,itemdb-shard-00-02-wclgk.mongodb.net:27017/test?ssl=true&replicaSet=ItemDB-shard-0&authSource=admin")
    db = client['ItemDB']

    if db:
        print("connected to db successfully")

    return db


def main():
    db = connect_to_database

    file_list = ["armors.json", "general_items.json", "magic_items.json", "weapons.json"]
    equip_json = []

    for file in file_list:
        equip_json.append(json.load(open(file)))
    # equip_file = open("equipment.json")
    # equip_json = json.load(equip_file)

    items = db.items
    items.delete_many({})
    for equip in equip_json:
        items.insert_many(equip)

    """
    # print(equip_json)
    # db.test.insert_many(equip_json)
    # print(len(equip_json))
    # test = equip_json[0]

    

    #print(len(db.items))

    # pprint.pprint(items.find_one({'name': "Buckler"}))"""
    pprint.pprint("Finished")


if __name__ == "main":
    main()
