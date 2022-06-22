import json
from pathlib import Path
import os

directory = os.path.dirname(os.path.realpath(__file__))
data_folder = "monsters/"


class Monster():
    '''The basic class for monsters, with misc data'''

    def __init__(self):
        self.name = None
        self.monster_type = None
        self.size = None
        self.alignment = None
        self.version = None
        self.combat_stats = combat_stats()

    def __str__(self):
        return str(self.__dict__)

        

    def set_misc(self, name, monster_type, size, alignment, version=None):
        '''
        Methode that allows the setting of misc data including:
            monstername:    string
            monstertype:    string
            size:           string
            alignment:      string
            version:        string?

        '''

        self.name = name
        self.monster_type = monster_type
        self.size = size
        self.alignment = alignment
        self.version = version

    def dictify(self): 
        mob_dict = {
            "name":                 self.name,
            "type":                 self.monster_type,
            "size":                 self.size,
            "alignment":            self.alignment,
            "version":              self.version,
            "armor_class":          self.combat_stats.armor_class,
            "armor_class_type":     self.combat_stats.armor_class_type,
            "passive_perception":   self.combat_stats.passive_perception,
            "hit_die_count":        self.combat_stats.hit_die_count,
            "hit_die_value":        self.combat_stats.hit_die_value,
            "hit_points_average":   self.combat_stats.hit_points_average,
            "str_score":            self.combat_stats.str_score,
            "dex_score":            self.combat_stats.dex_score,
            "con_score":            self.combat_stats.con_score,
            "int_score":            self.combat_stats.int_score,
            "wis_score":            self.combat_stats.wis_score,
            "cha_score":            self.combat_stats.cha_score,
        }
        return mob_dict

    def dumps(self):
        return json.dumps(self, indent=4, default=jdefault)

    def save_to_json(self):
        '''Methode that saves the monsters stats to a json-file'''

        Path(data_folder).mkdir(parents=True, exist_ok=True) 
        filename = self.name + ".json"
        file_to_open = directory / Path(data_folder + filename)
        f = open(file_to_open, "w+")
        dumped = self.dumps()
        f.write(dumped)



class combat_stats:
    '''The class for the combat stats of the monster'''

    def __init__(self):
        self.armor_class = None
        self.armor_class_type = None
        self.passive_perception = None
        self.hit_die_count = None
        self.hit_die_value = None
        self.hit_points_average = None
        self.str_score = None
        self.dex_score = None
        self.con_score = None
        self.int_score = None
        self.wis_score = None
        self.cha_score = None

    def __str__(self):
        return str(self.__dict__)

    def set_combat_values(self, armor_class, armor_class_type, passive_perception, hit_die_count, hit_die_value, hit_points_average):
        '''
        This Method sets values relevant to combat encounters like:
            armor class:        int
            armor calss type:   int
            passive perception: int
            hit die count:      int
            hit die value:      int
            hit points average: int

        You should only use integer values but who am I to judge if you want to mess with it
        '''
        self.armor_class = armor_class
        self.armor_class_type = armor_class_type
        self.passive_perception = passive_perception
        self.hit_die_count = hit_die_count
        self.hit_die_value = hit_die_value
        self.hit_points_average = hit_points_average

    def set_attribute_values(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        '''
        This Method sets values for attributes.
            strenght:       int
            dexterity:      int
            constitution:   int
            intelligence:   int
            wisdom:         int
            charisma:       int

        You should only use integer values but who am I to judge if you want to mess with it
        '''
        self.str_score = strength
        self.dex_score = dexterity
        self.con_score = constitution
        self.int_score = intelligence
        self.wis_score = wisdom
        self.cha_score = charisma


def jdefault(o):
    '''Methode to change the default handeling of json-dump for custom objects'''
    return o.__dict__

def create_monster_from_json(name):
    '''
    Methode that loads the stats for a monster from a json-file
    This method creates a new monster object each time it is called

    return: monster object
    '''

    filename = name + ".json"
    file_to_open = directory / Path(data_folder + filename)
    with open(file_to_open) as json_file:
        data = json.load(json_file)
        loaded_mob = Monster()
        loaded_mob.set_misc(data["name"], data["monster_type"], data["size"], data["alignment"], data["version"])
        combat_data = data["combat_stats"]
        loaded_mob.combat_stats.set_combat_values(  combat_data["armor_class"], combat_data["armor_class_type"], 
                                                    combat_data["passive_perception"], combat_data["hit_die_count"], 
                                                    combat_data["hit_die_value"], combat_data["hit_points_average"] )
        loaded_mob.combat_stats.set_attribute_values(   combat_data["str_score"], combat_data["dex_score"],combat_data["con_score"],
                                                        combat_data["int_score"],combat_data["wis_score"],combat_data["cha_score"])
    return loaded_mob




if __name__ == "__main__":

    test_monster = Monster()
    test_monster.set_misc("Tester", "Test_type", "universal", "true neutral", "1")
    test_monster.combat_stats.set_combat_values(0,0,0,0,0,0)
    test_monster.combat_stats.set_attribute_values(20,20,20,20,20,20)
    print(test_monster)
    print(test_monster.combat_stats)
    test_monster.save_to_json()
    mob = create_monster_from_json("Tester")

