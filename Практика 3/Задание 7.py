#-*- coding: utf-8 -*-
print("Введите число N")
n = int(input())
ft = 1
s = 0
def K(n, s, ft):
	if n > 0:
		for i in range(1, n + 1):
			ft *=  i
			s += ft
		print(s)	
K(n,s,ft)
