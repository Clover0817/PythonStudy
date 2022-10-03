for i in range(11):
	for s in range(11-i):
		print(" ", end='')
	for j in range(i * 2 + 1):
		print("*", end='')
	print()
