import tkinter as tk
import json
import encounter_mob as ecMob


''' The mainclass of the encounter handler'''

class Main_view():
    ''' The class wich handles the view of the menu'''
    def __init__(self, master):
        self.master = master
        master.title("Encounter Builder")

        self.lable = tk.Label(master, text="Welcome to the Encounter Builder!")
        self.lable.config(font=("Helvetica", 24))
        self.lable.pack()

        self.builder_button = tk.Button(master, text="Mob Builder")
        self.builder_button.config(font=("Helvetica", 18))
        self.builder_button.pack()
        self.builder_button.bind('<Button-1>', self.open_builder)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.config(font=("Helvetica", 18))
        self.quit_button.pack()
        
    def open_builder(self, event):
        win_builder = Mob_builder_view(root)
        

class Mob_builder_view(tk.Toplevel):
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.title("Mob Builder")
        self.fields = []
        self.entries = []
        self.smallFont = ("Helvetica", 16)
        
        lable = tk.Label(self, text="This is the Mob Builder")
        lable.config(font=("Helvetica", 24))
        lable.pack()

        fields = []
        filehandle = open("Encounter_Tool/settings/monster_fields.txt", 'r')
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
        clueLable = tk.Label(self, text="* This entry is mandatory")
        clueLable.config(font=("Helvetica", 12))
        clueLable.pack()

        self.save_mob_button = tk.Button(self, text="Build my Mob")
        self.save_mob_button.config(font=("Helvetica", 18))
        self.save_mob_button.pack()
        self.save_mob_button.bind('<Button-1>', self.save_mob()) 


    def save_mob(self):
        ent = []
        for entry in self.entries:
            value = entry.get()
            ent.append(value)

        new_mob = ecMob.monster()
        new_mob.set_misc(ent[0], ent[1], ent[2], ent[3], ent[4], ent[5])
        new_mob.combat_stats.set_combat_values(int(ent[6]), int(ent[7]), int(ent[8]), int(ent[9]), int(ent[10]), int(ent[11]))
        new_mob.combat_stats.set_attribute_values(int(ent[12]), int(ent[13]), int(ent[14]), int(ent[15]), int(ent[16]), int(ent[17]))
        new_mob.save_to_json()


        

root = tk.Tk()
menu = Main_view(root)
root.mainloop()