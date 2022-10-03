def max(*nums):
	maxN = -1
	for n in nums:
		if n >= maxN:
			maxN = n
	return maxN

print(max(1, 4, 6))
print(max(10, 5, 87, 57, 38))
print(max(4, 3, 2, 1))
