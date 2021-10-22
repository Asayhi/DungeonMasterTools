import tkinter as tk
import json
import queue
import random
import socket

maxSavedDices = 10

class die():

    def __init__(self):
        self.name = socket.getfqdn()
        self.sides = None
        self.value = None

    def set_sides(self, newSides):
        self.sides = newSides
    
    def roll(self):
        self.value = random.randint(1, self.sides)

     
class dice_view(tk.Toplevel):
    ''' 
        This class is an amalgumation of stuff to display a fillable form to create a mob
        that is saved as a json file via button click
    '''
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.title("Nicer Dicer")
        self.dice_queue = queue.Queue()
        self.entries = []
        self.rolls = tk.Frame(self)
        self.smallFont = ("Helvetica", 16)
        
        lable = tk.Label(self, text="Let's roll some die")
        lable.config(font=("Helvetica", 24))
        lable.pack()

        row = tk.Frame(self)
        lab = tk.Label(row, width=20, text="Number of Sides", anchor='w')
        lab.config(font=self.smallFont)
        self.userSides = tk.Entry(row, font=self.smallFont)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        self.userSides.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

        for field in self.dice_queue.queue:
            row = tk.Frame(self)
            lab = tk.Label(row, width=20, text=field, anchor='w')
            lab.config(font=self.smallFont)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)

        self.roll_button = tk.Button(self, text="Roll Die", command= lambda: self.roll())
        self.roll_button.config(font=("Helvetica", 18))
        self.roll_button.pack(side=tk.LEFT)

        self.exit_builder_button = tk.Button(self, text="Exit", command= lambda: self.exit())
        self.exit_builder_button.config(font=("Helvetica", 18))
        self.exit_builder_button.pack(side=tk.RIGHT)

    def roll(self):
        rolled_die = die()
        rolled_die.set_sides(int(self.userSides.get()))
        rolled_die.roll()
        self.dice_queue.put(rolled_die)
        self.update_rolls()

    def update_rolls(self):

        if self.dice_queue.qsize() > maxSavedDices:
            self.dice_queue.get()
        
        if not self.dice_queue.empty():
            self.rolls.pack_forget()
            self.rolls.destroy()

        self.rolls = tk.Frame(self)

        for rolled in self.dice_queue.queue:
            row = tk.Frame(self.rolls)
            lab = tk.Label(row, width=40, text="Value: "+str(rolled.value)+" Type: "+str(rolled.sides)+" Roller: "+str(rolled.name), anchor='w')
            lab.config(font=self.smallFont)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)

        self.rolls.pack(side=tk.TOP)


    def exit(self):
        self.destroy()
        self.update()
   

if __name__ == "__main__":
    root = tk.Tk()
    menu = dice_view(root)
    root.mainloop()
     