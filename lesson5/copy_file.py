import os
import shutil
def cp_file():
	try:
		name = os.path.splitext(__file__)[0]
		shutil.copy(__file__,name + '_copy.py')
		print('файл скрипта скопирован')
	except OSError:
		print('не удалось скопировать файл')

if __name__ == '__main__':
	cp_file()