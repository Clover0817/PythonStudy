nums = input("숫자 두 개를 입력하세요: ")
num = nums.split()

num[0] = int(num[0])
num[1] = int(num[1])
try:
	result = num[0] / num[1]
	print(result)
except ZeroDivisionError:
	print("division by zero")
