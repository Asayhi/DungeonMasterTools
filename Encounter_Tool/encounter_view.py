import tkinter as tk
import json
import Encounter_Tool.encounter_mob as ecMob
     
class Mob_builder_view(tk.Toplevel):
    ''' 
        This class is an amalgumation of stuff to display a fillable form to create a mob
        that is saved as a json file via button click
    '''
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.title("Mob Builder")
        self.fields = []
        self.entries = []
        self.smallFont = ("Helvetica", 16)
        self.bigFont = ("Helvetica", 24)
        self.configPath = "Encounter_Tool/settings/monster_fields.txt"
        
        lable = tk.Label(self, text="This is the Mob Builder")
        lable.config(font=self.bigFont)
        lable.pack()

        fields = []
        filehandle = open(self.configPath, 'r')
        filecontents = filehandle.readlines()

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
        self.clueLable = tk.Label(self, text="* This entry is mandatory")
        self.clueLable.config(font=("Helvetica", 12))
        self.clueLable.pack()

        self.save_mob_button = tk.Button(self, text="Build my Mob", command= lambda: self.save_mob())
        self.save_mob_button.config(font=("Helvetica", 18))
        self.save_mob_button.pack(side=tk.LEFT)

        self.exit_builder_button = tk.Button(self, text="Exit", command= lambda: self.exit())
        self.exit_builder_button.config(font=("Helvetica", 18))
        self.exit_builder_button.pack(side=tk.RIGHT)


    def save_mob(self):
        ent = []
        for entry in self.entries:
            value = entry.get()
            ent.append(value)

        if len(self.entries[0].get()) == 0:
            self.clueLable.config(fg='red', text='Mandatory Parts missing!')

        else:
            new_mob = ecMob.monster()
            new_mob.set_misc(ent[0], ent[1], ent[2], ent[3], ent[4])
            new_mob.combat_stats.set_combat_values(int(ent[5]), int(ent[6]), int(ent[7]), int(ent[8]), int(ent[9]), int(ent[10]))
            new_mob.combat_stats.set_attribute_values(int(ent[11]), int(ent[12]), int(ent[13]), int(ent[14]), int(ent[15]), int(ent[16]))
            new_mob.save_to_json()

    def exit(self):
        self.destroy()
        self.update()
   
