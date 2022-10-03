num = "901231-1914983"

index = num.find("-")
year, sex = num[:2], int(num[index+1])

if (sex == 1 or sex == 3):
	sex = "남자"
else:
	sex = "여자"

print(year + "년생 " +  sex)
