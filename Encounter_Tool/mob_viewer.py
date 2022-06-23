from pprint import pprint
import tkinter as tk
from pymongo import MongoClient

if __name__ == "__main__":
    import encounter_mob as ecMob
    import mongo_mob_connector as connect

else:
    import Encounter_Tool.encounter_mob as ecMob
    import Encounter_Tool.mongo_mob_connector as connect

class Mob_Viewer(tk.Toplevel):
    ''' 
        This class is an amalgumation of stuff to display a mob
        that is saved in a mongo db via button click
    '''
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.title("Mob Viewer")
        self.fields = []
        self.entries = []
        self.smallFont = ("Helvetica", 16)
        self.bigFont = ("Helvetica", 24)
        self.configPath = "Encounter_Tool/settings/monster_fields.txt"

        monster_list = self.getAllEntries()
        self.monster_names = []
        for name in monster_list:
            self.monster_names.append(name["name"])
        pprint(monster_list)
        pprint(self.monster_names)
        self.clicked = tk.StringVar(self.monster_names[0])

        lable = tk.Label(self, text="This is the Mob Viewer")
        lable.config(font=self.bigFont)
        lable.pack()

        fields = []
        filehandle = open(self.configPath, 'r')
        filecontents = filehandle.readlines()

        dropList = tk.OptionMenu(self, self.clicked, *self.monster_names)
        dropList.pack()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            current_place = line[:-1]

            # add item to the list
            fields.append(current_place)

        filehandle.close()
        self.fields = fields
        entries = []
        for field in self.fields:
            row = tk.Frame(self)
            lab = tk.Label(row, width=20, text=field, anchor='w')
            lab.config(font=self.smallFont)
            ent = tk.Entry(row, font=self.smallFont)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append(ent)

        self.entries = entries

        self.load_mob_button = tk.Button(self, text="Load my Mob", command= lambda: self.load_mob())
        self.load_mob_button.config(font=("Helvetica", 18))
        self.load_mob_button.pack(side=tk.LEFT)

        self.exit_builder_button = tk.Button(self, text="Exit", command= lambda: self.exit())
        self.exit_builder_button.config(font=("Helvetica", 18))
        self.exit_builder_button.pack(side=tk.RIGHT)

    def load_mob(self):
        pass

    def getAllEntries(self):
        client = MongoClient(port=27017)
        db = client.monsters
        collection = db['monsters']
        cursor = collection.find({}, {"name":1, "_id":0})
        return cursor

if __name__ == "__main__":
    root = tk.Tk()
    menu = Mob_Viewer(root)
    root.mainloop()