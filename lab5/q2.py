def list_to_dic(keys, values):
	return {key : value for key, value in zip(keys, values)}

a = []
b = []

for i in range(1, 11):
	a.append(i)
	b.append(i ** 2)
dic = list_to_dic(a, b)
print(dic[6])
