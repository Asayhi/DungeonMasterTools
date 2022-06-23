import tkinter as tk
import Encounter_Tool.encounter_view as enc
from Encounter_Tool.mob_viewer import Mob_Viewer
from dice.dice_view import dice_view

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

        self.viewer_button = tk.Button(master, text="Mob Viewer")
        self.viewer_button.config(font=("Helvetica", 18))
        self.viewer_button.pack()
        self.viewer_button.bind('<Button-1>', self.open_viewer)

        self.dice_button = tk.Button(master, text="Dice Roller")
        self.dice_button.config(font=("Helvetica", 18))
        self.dice_button.pack()
        self.dice_button.bind('<Button-1>', self.open_roll)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.config(font=("Helvetica", 18))
        self.quit_button.pack()
        
    def open_builder(self, event):
        win_builder = enc.Mob_builder_view(root)

    def open_roll(self, event):
        win_builder = dice_view(root)

    def open_viewer(self, event):
        win_builder = Mob_Viewer(root)
   
if __name__ == "__main__":
    root = tk.Tk()
    menu = Main_view(root)
    root.mainloop()
     