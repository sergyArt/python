import os
def del_dir(*args):
	try:
		[os.rmdir(i) for i in args]
	except OSError:
		print('не удалось удалить папки')
	else:
		print('папки успешно удалены')


if __name__ == '__main__':
	del_dir('dir_1','dir_2','dir_3','dir_4','dir_5','dir_6','dir_7','dir_8','dir_9',)