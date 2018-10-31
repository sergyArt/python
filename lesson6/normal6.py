class Person:
    def __init__(self, name, surname, patronymic):
        self._name = name
        self._surname = surname
        self._patronymic = patronymic

    def get_full_name(self):
        return self._surname + ' ' +  self._name + ' ' + self._patronymic

class Student(Person):
    def __init__(self, name, surname, patronymic, class_room, mother, father):
        Person.__init__(self, name, surname, patronymic)
        self._class_room = {'class_num': int(class_room[0]),
                            'class_char': class_room[1]}
        self._mother = mother
        self._father = father

    @property
    def get_parents(self):
        return print('Мать ученика: {}, Отец ученика: {}'.format(self._mother, self._father))

    @property
    def class_room(self):
        return "{}{}".format(self._class_room['class_num'], self._class_room['class_char'])

    def get_subjects(self, teacher):
        #print(self.class_room, teacher.get_teach_classes)
        if self.class_room in teacher.get_teach_classes:
            print("{} -> {} -> {} -> {}".format(self.get_full_name(),self.class_room,teacher.get_full_name(),teacher.get_schsubjects))




class Teacher(Person):
    def __init__(self, name, surname, patronymic, teach_classes, schsubject):
        Person.__init__(self, name, surname, patronymic)
        self._teach_classes = list(map(self.convert_class,teach_classes.split()))
        self._schsubject = schsubject

    @property
    def get_teach_classes(self):
        list_classes = []
        for i in self._teach_classes:
            list_classes.append('{}{}'.format(i['class_num'],i['class_char']))
        return list_classes

    @property
    def get_schsubjects(self):
        return self._schsubject

    def teach_this_class(self, class_):
        return True if class_ in self.get_teach_classes else False

    def convert_class(self,class_room):
        return {'class_num' : int(class_room[0]),
                'class_char' : class_room[1]}


student1 = Student('Василий','Иванов','Сергеевич','9А','Иванова Нина Николаевна','Иванов Андрей андреевич')
student2 = Student('Сергей','Васильев','Александрович','7Б', 'Васильева Ирина Сергеевна','Васильев Андрей Игоревич')
student3 = Student('Матвей','Петров','Леонидович','7Б', 'Петрова Людмила Ивановна','Петров Борис Павлович')
student4 = Student('Иван','Куликов','Леонидович','7А', 'Куликова Людмила Ивановна','Куликов Борис Павлович')
student5 = Student('Матвей','Сидоров','Леонидович','9Б', 'Сидорова Людмила Ивановна','Сидоров Борис Павлович')

students = [student1,student2,student3,student4,student5]


teacher1 = Teacher('Лев','Васильев','Николаевич','9А 7Б','математика')
teacher2 = Teacher('Игорь','Петров','Сергеевич','9А','физика')
teacher3 = Teacher('Дмитрий','Ивашкин','Вячеславович','9Б 7А','литература')
teachers = [teacher1,teacher2,teacher3]



if __name__ == '__main__':
    class_school = []
    for i in students:
        class_school.append(i.class_room)
    print('В школе имеются классы: ', list(set(class_school)))

    print('Список учеников класса {}: '.format('7Б'))
    for id,i in enumerate(students):
        if i.class_room == '7Б':
            print(id,'. ',i.get_full_name())

    print('Список предметов для ученика {}: '.format(student1.get_full_name()))
    for i in teachers:
        student1.get_subjects(i)


    print('Родители ученика {}'.format(student1.get_full_name()))
    student1.get_parents


    print('Список учителей, преподающих в классе {}:'.format('9Б'))
    for i in teachers:
        if i.teach_this_class('9Б'):
            print(i.get_full_name())





