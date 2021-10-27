#-*- coding: utf-8 -*-
print("Введите число N")
n = int(input())
s = 1
def K(n, s):
	if n > 0:
		for i in range(1, n + 1):
			s = s * i
		print(s)	
K(n, s)