import os
def list_dir(name):
	try:
		[print(i) for i in os.listdir(name) if os.path.isdir(i)]
	except OSError:
		print('не удалось отобразить папки')
	


if __name__ == '__main__':
	list_dir(os.getcwd())
	list_dir('TEST')