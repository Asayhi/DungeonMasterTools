from unittest import result
from pymongo import MongoClient
from pprint import pprint
import encounter_mob as mob

def save_mob_to_db(monster):
    client = MongoClient(port=27017)
    print("Connection Successful")
    db = client.monsters
    mob = monster.dictify()
    print(mob)
    print(monster)
    result = db.monsters.insert_one(mob)

    pprint(result)

    client.close()


if __name__ == "__main__":

    test_monster = mob.monster()
    test_monster.set_misc("Tester", "Test_type", "universal", "true neutral", "1")
    test_monster.combat_stats.set_combat_values(0,0,0,0,0,0)
    test_monster.combat_stats.set_attribute_values(20,20,20,20,20,20)
    save_mob_to_db(test_monster)
