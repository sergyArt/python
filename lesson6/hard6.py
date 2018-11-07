


class Worker:
    def __init__(self,line):
        self._worker_data = list(filter(None,(line.replace('\n','')).split(' ')))
        self._name = self._worker_data[0]
        self._surname = self._worker_data[1]
        self._salary = self._worker_data[2]
        self._position = self._worker_data[3]
        self._norm = self._worker_data[4]


    def get_salary(self):
        hours_work = []
        with open('hours_of','r') as file:
            for linenum, line in enumerate(file):
                if linenum > 0:
                    hours_work.append(list(filter(None,(line.replace('\n','')).split(' '))))


        for j in hours_work:
            if j[0] == self._name and j[1] == self._surname:
                if int(self._norm) == int(j[2]):
                    print('Сотрудник ', self._name, self._surname, ' получает зарплату ', self._salary)
                elif int(j[2]) < int(self._norm):
                    salary_of_hour = round(float(self._salary) / float(self._norm))
                    hours = int(self._norm) - int(j[2])
                    print('Сотрудник ', self._name, self._surname, ' получает зарплату ', float(self._salary) - (float(hours) * salary_of_hour),'р')
                elif int(j[2]) > int(self._norm):
                    salary_of_hour = round(float(self._salary) / float(self._norm))
                    hours = int(j[2]) - int(self._norm)
                    print('Сотрудник ', self._name, self._surname, ' получает зарплату ', float(self._salary) + 2 * float(hours) * salary_of_hour,'р')









if __name__ == '__main__':
    lst = []
    with open('workers','r') as file:
        for linenum,line in enumerate(file):
            if linenum > 0:
                lst.append(Worker(line))


    for i in lst:
        i.get_salary()