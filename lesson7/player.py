from card import Card

class Player:
    def __init__(self, name):
        self._name = name
        self._card = Card()

    @property
    def card(self):
        self._card.show_card

    def step(self, value, barrel_number):
        # 1 - Y, 2 - N
        if value == 'Y' or value == 'y':
            if self._card.number_is_true(barrel_number):
                self._card.remove_number(barrel_number)
                return True
            else:
                return False
        else:
            if self._card.number_is_true(barrel_number):
                return False
            else:
                return True

    def empty_card(self):
        return self._card.is_no_number()


if __name__  == '__main__':
    player = Player('MAX')
    player.card
    print(player.step('Y',23))
    player.card