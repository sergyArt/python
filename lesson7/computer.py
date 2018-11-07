import random
from player import Player

class Computer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def show_name(self):
        return self._name

    def step(self, barrel_number):
        generate_answer = random.randint(0,1)
        value = 'Y' if generate_answer == 1 else 'N'
        return Player.step(self, value, barrel_number)

    def empty_card(self):
        return Player.empty_card(self)

if __name__ == '__main__':

    comp = Computer('SERGY')
    comp.card
    comp.step(23)
    comp.card