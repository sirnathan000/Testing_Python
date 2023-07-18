import os
current_path = os.path.dirname(__file__)
print(current_path)

def prompt(message):
	while True:
		try:
			inp = input(message)
		except Exception:
			print('invalide input')
			continue
		if " " in inp:
			print("no, spaces allowed")
			continue
		else:
			return inp

inp = prompt("name a directory : ")
alt_path = current_path + "/" + inp
print(alt_path)
if not os.path.exists(alt_path):
	os.mkdir(alt_path)
