import json

sum = 0
with open('movie.json') as datafile:
	jsondata = json.load(datafile)
	movielist = jsondata['movie']
	
	for movie in movielist:
		sum += int(movie['salesAmt'])
print("오늘 매출액은 총", sum, "원")
