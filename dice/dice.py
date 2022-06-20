import random
import socket

class die():

    def __init__(self):
        self.name = socket.gethostname()
        self.sides = None
        self.value = None

    def __str__(self) -> str:
        return str(self.__dict__)

    def set_sides(self, newSides):
        try:
            self.sides = newSides

        except:
            self.sides = None
 
    def roll(self):
        try:
            self.value = random.randint(1, self.sides)

        except:
            print("Someone did not set any sides for this dice")
            pass

    def send(self):
        pass
