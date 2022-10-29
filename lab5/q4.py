fname = input("Enter file name:")
dic = {}

with open(fname, 'rt') as fp:
	while True:
		data = fp.readline()
		if not data: break

		if data.startswith("From: "):
			fields = data.split()
			if fields[1] in dic:
				dic[fields[1]] += 1
			else:
				dic[fields[1]] = 1
print(dic)
