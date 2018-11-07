import random
class Barrel:
    def __init__(self):
        self._numbers = []
        [self._numbers.append(i) for i in range(1,91)]
        random.shuffle(self._numbers)

    def show(self):
        [print(i) for i in self._numbers]

    def next(self):
        return self._numbers.pop(0) if len(self._numbers) > 0 else None



if __name__ == '__main__':
    barrel = Barrel()
    barrel.show()
    print('Return next',barrel.next())
    print('Return next', barrel.next())