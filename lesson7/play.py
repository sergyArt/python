from human import Human
from computer import Computer
from barrel import Barrel

class Play:
    def __init__(self, *players):
        self._barrel = Barrel()
        self._game_players = []
        for i in players:
            self._game_players.append(Human(i))
        self._comp = Computer('Computer')
        print('Players: ')
        for i in self._game_players:
            print(i.show_name())


    def new_game_comp(self):
        try:
            continue_ = True
            finish_ = False
            while True:
                barrel_number = self._barrel.next()
                if not barrel_number:
                    break
                print('Выпал бочонок с номером: ', barrel_number)
                print('Карточка игрока: ')
                [i.card for i in self._game_players]
                print('Карточка компьютера: ')
                self._comp.card
                #[i.step(barrel_number) for i in self._game_players]
                for i in self._game_players:
                    print('Ход игрока {}'.format(i.show_name()))
                    if not i.step(barrel_number):
                        name = i.show_name()
                        continue_ = False
                        break
                if not continue_:
                    print('Игра окончена. Игрок {} проиграл.'.format(name))
                    break
                print('Ход игрока {}'.format(self._comp.show_name()))
                if not self._comp.step(barrel_number):
                   print('Игра окончена. Игрок {} проиграл.'.format(self._comp.show_name()))
                   break
                for i in self._game_players:
                    if i.empty_card():
                        name_ = i.show_name()
                        finish_ = True
                        break
                if self._comp.empty_card():
                    print('Игра окончена. Победил игрок {}.'.format(self._comp.show_name()))
                    break
                if finish_:
                    print('Игра окончена. Победил игрок {}'.format(name_))
                    break
        except KeyboardInterrupt:
            print('\n')
            print('Игра прервана. Выход.... ')

    def new_game_players(self):
        try:
            continue_ = True
            finish_ = False
            while True:
                barrel_number = self._barrel.next()
                if not barrel_number:
                    break
                print('Выпал бочонок с номером: ', barrel_number)
                print('Карточка игрока: ')
                [i.card for i in self._game_players]
                for i in self._game_players:
                    print('Ход игрока {}'.format(i.show_name()))
                    if not i.step(barrel_number):
                        name = i.show_name()
                        continue_ = False
                        break
                if not continue_:
                    print('Игра окончена. Игрок {} проиграл.'.format(name))
                    break
                for i in self._game_players:
                    if i.empty_card():
                        name_ = i.show_name()
                        finish_ = True
                        break
                if finish_:
                    print('Игра окончена. Победил игрок {}'.format(name_))
                    break
        except KeyboardInterrupt:
            print('\n')
            print('Игра прервана. Выход.... ')



if __name__ == '__main__':
    #Для запуска игры с компьютером передаем в конструктор имя одного игрока и используем мметод new_game_comp
    play = Play('SERGY')
    play.new_game_comp()
    #Для запуска игры между игроками передаем в конструктор имена игроков через запятую и используем метод new_game_players
    play1 = Play('SERGY','MAX')
    play1.new_game_players()
