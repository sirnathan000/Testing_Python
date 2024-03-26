import os
import time

f = open('file.csv')
f.seek(0, os.SEEK_END)

while True:
	line = f.readline()
	if line == '':
		time.sleep(0.1)
		continue
	else:
		print(line)
