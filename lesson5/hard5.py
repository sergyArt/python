# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp  <file_name> - создание копии файла")
    print("rm  <file_name> - удаление файла")
    print("cd <full_path or relative_path> - меняет текущую папку на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        shutil.copy(dir_name,'copy_' + dir_name)
        print('файл {}  скопирован'.format(dir_name))
    except IOError:
        print('ошибка копирования файла {}'.format(dir_name))

def move_to_dir():
    #print(dir_name)
    if not dir_name:
        print("Необходимо указать путь к папке вторым параметром")
        return
    try:
        os.chdir(os.path.abspath(dir_name))
        print('успешно перешли в папку {}'.format(os.getcwd()))
    except OSError:
        print('ошибка во время перемещения')

def del_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    answer = input('Вы уверены что хотите удалить файл {} ? Y/N :'.format(dir_name))
    if answer == 'Y':
        try:
            os.remove(dir_name)
            print('файл {} успешно удален'.format(dir_name))
        except OSError:
            print('ошибка удаления файла {}'.format(dir_name))

def list_path():
    try:
        print('абсолютный путь к текущей директории: {} '.format(os.path.abspath(os.getcwd())))
    except OSError:
        print('ошибка определения пути')



do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp" : copy_file,
    "rm" : del_file,
    "cd" : move_to_dir,
    "ls" : list_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")