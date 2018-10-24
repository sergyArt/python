import os

def new_dir(*args):
	try:
		[os.mkdir(i) for i in args]
	except OSError:
		print('не удалось создать папк-(и)')
	else:
		print('папк-(и) успешно созданы')


def del_dir(*args):
	try:
		[os.rmdir(i) for i in args]
	except OSError:
		print('не удалось удалить папк-(и)')
	else:
		print('папк-(и) успешно удалены')

def list_dir(name):
	try:
		[print(i) for i in os.listdir(name) if os.path.isdir(i)]
	except OSError:
		print('не удалось отобразить папк-(и)')

def move_dir(path):
	try:
		os.chdir(path)
		print('успешно перешли в папку {}'.format(path))
	except OSError:
		print('невозможно перейти')
	
if __name__ == '__main__':
	pass