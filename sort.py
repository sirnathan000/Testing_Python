import os

search = os.path.dirname(__file__)
#print(search)
files =  filter(os.path.isfile, os.listdir(search))
files = [os.path.join(search, f) for f in files]
print(files)
files.sort(key=lambda x: os.path.getmtime(x))
print(files)
