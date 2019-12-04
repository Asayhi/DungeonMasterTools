import json
from pathlib import Path

cwd = Path.cwd()
data_folder = "monsters/"


class monster():
    '''The basic class for monsters, with misc data'''

    def __init__(self):
        self.name = None
        self.monster_tpye = None
        self.size = None
        self.alignment = None
        self.version = None
        self.sub_type = None

    def __str__(self):
        return str(self.__dict__)

    def create_combat_stats(self):
        self.combat_stats = combat_stats()

    def set_misc(self, name, monster_type, size, alignment, version=None , subtype = None):
        self.name = name
        self.monster_tpye = monster_type
        self.size = size
        self.alignment = alignment
        self.version = version
    
    def save_to_json(self):
        '''Methode that saves the monsters stats to a json-file'''
        Path(data_folder).mkdir(parents=True, exist_ok=True) 
        filename = self.name + ".json"
        file_to_open = cwd / Path(data_folder + filename)
        f = open(file_to_open, "w+")
        json.dump(self, f, indent=4, default=jdefault)


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
            This Method sets values like armor and hit die.
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
    '''Methode that loads the stats for a monster from a json-file'''
    filename = name + ".json"
    file_to_open = cwd / Path(data_folder + filename)
    with open(file_to_open) as json_file:
        data = json.load(json_file)
        loaded_mob = monster()
        loaded_mob.set_misc(data['name'], data['monster_type'], data['size'], data['alignment'], data['version'])
        loaded_mob.combat_stats.set_combat_values(data['armor_class'], data['armor_class_type'], data['passive_perception'], data['hit_die_count'], data["hit_die_value"], data["hit_die_average"] )
        loaded_mob.combat_stats.set_attribute_values(20,20,20,20,20,20)




if __name__ == "__main__":
    try:
        test_monster = monster()
        test_monster.create_combat_stats()
        test_monster.set_misc("Tester", "Test_type", "universal", "true neutral", "1")
        test_monster.combat_stats.set_combat_values(0,0,0,0,0,0)
        test_monster.combat_stats.set_attribute_values(20,20,20,20,20,20)
        print(test_monster)
        print(test_monster.combat_stats)
        test_monster.save_to_json()
        #load_from_json("Tester")

    except Exception as e:
        print("Test Faild with Error:\n")
        print(e)
