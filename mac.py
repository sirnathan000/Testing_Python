import re
 
# Function to validate MAC address.
 
 
def testMACAddress(str):
 
    # Regex to check valid
    # MAC address
    regex = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")
 
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return please enter a value
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    elif(re.search(p, str)):
        return True
    else:
        return False



def Openfile(str):
	f = open(str, "r")
	lines=f.readline()
	print(lines)
	 
if __name__ == '__main__':
	while True:
		try:
			Mac = input("please enter a mac address: ")
			if (testMACAddress(Mac)):
				print(Mac + " will be used for input")
				Path = input("please enter path: ")
				Openfile(Path)
				break
			else:
				print("invalid input")
				continue
		except Exception as e: 
			print("error " + e)
			continue
	
	print("continue 1")
	
