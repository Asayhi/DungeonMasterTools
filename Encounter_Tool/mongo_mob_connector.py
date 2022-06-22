from unittest import result
from json5 import load
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
    data = db.find_one({"name": name})
    loaded_mob = mob.Monster()
    loaded_mob.set_misc(data["name"], data["monster_type"], data["size"], data["alignment"], data["version"])
    combat_data = data["combat_stats"]
    loaded_mob.combat_stats.set_combat_values(  combat_data["armor_class"], combat_data["armor_class_type"], 
                                                combat_data["passive_perception"], combat_data["hit_die_count"], 
                                                combat_data["hit_die_value"], combat_data["hit_points_average"] )
    loaded_mob.combat_stats.set_attribute_values(   combat_data["str_score"], combat_data["dex_score"],combat_data["con_score"],
                                                    combat_data["int_score"],combat_data["wis_score"],combat_data["cha_score"])
    return loaded_mob



if __name__ == "__main__":

    test_monster = mob.Monster()
    test_monster.set_misc("Tester", "Test_type", "universal", "true neutral", "1")
    test_monster.combat_stats.set_combat_values(0,0,0,0,0,0)
    test_monster.combat_stats.set_attribute_values(20,20,20,20,20,20)
    save_mob_to_db(test_monster)
    load_mob_from_db("Tester")
