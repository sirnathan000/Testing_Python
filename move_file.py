import os
import datetime
import shutil
import time

def get_files():
	files = []
	cur_dir = os.getcwd()
	with open("/home/nate/script.txt", 'rt') as file:
		for line in file:
			files.append(str.strip(cur_dir + '/' +line))
	return files

def get_all_files_dir():
	cur_dir = os.getcwd()
	dir = os.listdir(cur_dir)
	test = '/home/nate/test_for_dir'
	for thing in dir:
		cr_path = cur_dir + '/' + thing
		if os.path.isfile(cr_path):
			print(cr_path)
		elif os.path.exists(test):
			print(test)
		elif not os.path.exists(test):
			print('file does not exist')
	#print(dir)

def move_files(list1):
	print(list1)
	cur_dir = os.getcwd()
	file_path = cur_dir + '/' + list1[0]
	move_path = cur_dir + '/move'
#	shutil.move(file_path, move_path)

def get_info(file):
	print(file)
	for num in range(len(file)):
		t = os.path.getctime(file[num])
		#with datetime
		get_time = datetime.datetime.fromtimestamp(t)
		#with time
		t2 = time.ctime(t)
		obj = time.strptime(t2)
		stamp = time.strftime("%Y-%m-%d %H:%M:%S", obj)
		stamp2 = time.strftime("%Y", obj)
		print(stamp)
		print(stamp2)
		print(get_time)

if __name__ == '__main__':
	get_all_files_dir()
	get_info(get_files())
	move_files(get_files())

#print(os.listdir())
