title = input()
with open(title, "rt") as f1:
	f2 = open("output.txt", "wt")
	while True:
		str = f1.readline()
		if not str: break
		f2.write(str.upper())	
	f2.close()
