# -*- coding: utf-8 -*-
print("Введите число n =< 9")
n = int(input())
def K(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print(j, end = "")
		print('\n')
K(n)