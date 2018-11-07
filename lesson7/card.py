import random
class Card:
    def __init__(self):

        def line():
            result = []
            seen = set()
            for i in range(1,28):
                x = random.randint(1,90)
                while x in seen:
                    x = random.randint(1,90)
                seen.add(x)
                result.append(x)
            result.sort()
            return result

        def add_space(line):
            no_num = []
            sen = set()
            for j in range(1,5):
                y = random.randint(0,7)
                while y in sen:
                    y = random.randint(0,7)
                sen.add(y)
                no_num.append(y)
            for i in no_num:
                line.pop(i)
                line.insert(i,' ')
            return line

        line = line()
        line1 = add_space(line[:9])
        line2 = add_space(line[9:18])
        line3 = add_space(line[18:])
        self._card_list1 = []
        self._card_list = []
        self._card_list1.extend(line1)
        self._card_list1.extend(line2)
        self._card_list1.extend(line3)
        for i in self._card_list1:
            self._card_list.append(str(i))


    @property
    def show_card(self):
        print('------------------------------')
        flag = 0
        for i in self._card_list:
            print(i, end=' ')
            flag += 1
            if flag == 9:
                print('\n')
                flag = 0
        print('------------------------------')



    def number_is_true(self, number):
        flag = False
        for i in self._card_list:
            if i == str(number):
                flag = True
        return flag

    def remove_number(self, number):
        for id, i in enumerate(self._card_list):
            if i == str(number):
                self._card_list.pop(id)
                self._card_list.insert(id, '-')


    def is_no_number(self):
        return True if len(list(filter(lambda x: (x != ' ') and (x != '-'),self._card_list))) == 0 else False


if __name__ == '__main__':
    card = Card()
    card.show_card
    card.remove_number(23)
    card.show_card
    print(card.is_no_number())
    print(card.number_is_true(11))