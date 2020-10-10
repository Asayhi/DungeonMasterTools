import tkinter as tk

class mob_builder_view():
    def __init__(self, master):
        self.master = master
        master.title("Mob Builder")
        self.lable = tk.Label(self, text="This is a new window")
        self.lable.config(font=("Helvetica", 24))
        self.lable.pack()
    