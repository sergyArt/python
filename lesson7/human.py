from player import Player

class Human(Player):
    def __init__(self, name):
        Player.__init__(self, name)


    def show_name(self):
        return self._name


    def step(self, barrel_number):
        rigth = False
        while rigth == False:
            value = input('Зачеркнуть? Y/N ')
            if value == 'Y' or value == 'N' or value == 'n' or value == 'y':
                rigth = True
                return Player.step(self, value, barrel_number)
            else:
                print('Неверное значение. Попробуйте еще раз!')

    def empty_card(self):
        return Player.empty_card(self)

if __name__ == '__main__':

    human = Human('SERGY')
    print(human.show_name())
    human.card
    human.step(23)
    human.card