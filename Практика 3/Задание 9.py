# -*- coding: utf-8 -*-
print("Введите число n")
n = int(input())
f1 = f2 = 1
def K(f1, f2, n):
	for i in range(2, n):
		f1, f2 = f2, f1 + f2 
		print(f2, end = ' ')
K(f1, f2, n)