import easy
import os
import signal

def console_utility():
	while True:
		try:
			print('1.перейти в папку')
			print('2.посмотреть содержимое папки')
			print('3.удалить папку')
			print('4.создать папку')
			print('Нажмите Ctrl + C для выхода')
			answer = int(input('Введите пункт меню:'))
			if answer == 1:
				folder_name = input('Введите имя папки:')
				easy.move_dir(folder_name)
				input('Нажмите любую клавишу для продолжения')
			elif answer == 2:
				easy.list_dir(os.getcwd())
				input('Нажмите любую клавишу для продолжения')
			elif answer == 3:
				folder_name = input('Введите имя папки:')
				easy.del_dir(folder_name)
				input('Нажмите любую клавишу для продолжения')
			elif answer == 4:
				folder_name = input('Введите имя папки:')
				easy.new_dir(folder_name)
				input('Нажмите любую клавишу для продолжения')
			else:
				print('Неверный номер пункта. Попробуйте еще раз')
		except KeyboardInterrupt:
			print('\n')
			print('exit....')
			break
		except Exception:
			print('!')
			break


if __name__ == '__main__':
	console_utility()