F = [0 for i in range(100)]

def fib_opt(n):
	if (n == 1 or n == 2):
		return 1
	if F[n-1] == 0:
		F[n-1] = fib_opt(n-1)
	if F[n-2] == 0:
		F[n-2] = fib_opt(n-2)

	return F[n-1] + F[n-2]

print(fib_opt(5))
print(fib_opt(10))
print(fib_opt(35))
