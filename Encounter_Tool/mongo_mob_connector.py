from unittest import result
from pymongo import MongoClient
from pprint import pprint
import encounter_mob as mob

def save_mob_to_db(monster: mob.Monster):
    client = MongoClient(port=27017)
    print("Connection Successful")
    db = client.monsters
    mob = monster.dictify()
    print(mob)
    print(monster)
    result = db.monsters.insert_one(mob)

    pprint(result)

    client.close()

def load_mob_from_db(name: str):
    client = MongoClient(port=27017)
    db = client.monsters
    data = db.monsters.find_one({"name": name})
    loaded_mob = mob.Monster()
    loaded_mob.set_misc(data["name"], data["type"], data["size"], data["alignment"], data["version"])

    loaded_mob.combat_stats.set_combat_values(  data["armor_class"], data["armor_class_type"], 
                                                data["passive_perception"], data["hit_die_count"], 
                                                data["hit_die_value"], data["hit_points_average"] )
    loaded_mob.combat_stats.set_attribute_values(   data["str_score"], data["dex_score"], data["con_score"],
                                                    data["int_score"], data["wis_score"], data["cha_score"])
    return loaded_mob



if __name__ == "__main__":

    test_monster = mob.Monster()
    test_monster.set_misc("Tester", "Test_type", "universal", "true neutral", "1")
    test_monster.combat_stats.set_combat_values(0,0,0,0,0,0)
    test_monster.combat_stats.set_attribute_values(20,20,20,20,20,20)
    save_mob_to_db(test_monster)
    test_mob = load_mob_from_db("Tester")
    print("Ended")
