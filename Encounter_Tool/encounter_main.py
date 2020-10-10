import tkinter as tk
import json
import encounter_mob_builder as builder

''' The mainclass of the encounter handler'''

class main_View():
    ''' The class wich handles the view of the menu'''
    def __init__(self, master):
        self.master = master
        master.title("Encounter Builder")

        self.lable = tk.Label(master, text="Welcome to the Encounter Builder!")
        self.lable.config(font=("Helvetica", 24))
        self.lable.pack()

        self.builder_button = tk.Button(master, text="Mob Builder", command=self.open_builder)
        self.builder_button.config(font=("Helvetica", 18))
        self.builder_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.config(font=("Helvetica", 18))
        self.quit_button.pack()
        
    def open_builder(self):
        builder.mob_builder_view()

root = tk.Tk()
my_gui = main_View(root)
root.mainloop()