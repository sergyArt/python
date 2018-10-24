import os
def new_dir(*args):
	try:
		[os.mkdir(i) for i in args]
	except OSError:
		print('не удалось создать папки')
	else:
		print('папки успешно созданы')


if __name__ == '__main__':
	new_dir('dir_1','dir_2','dir_3','dir_4','dir_5','dir_6','dir_7','dir_8','dir_9',)

			