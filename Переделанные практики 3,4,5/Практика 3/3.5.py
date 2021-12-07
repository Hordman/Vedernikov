n = int(input())
s = 0
def K(n, s):
	if n > 0:
		for i in range(1, n + 1):
			s += i ** 3
		print(s)	
K(n, s)