# -*- coding: utf-8 -*-
print("Введите число n")
n = int(input())
k = int(input())
f1 = f2 = 1
def C(f1, f2, n, k):
	for i in range(2, n):
		f1, f2 = k, f1 + f2
		print(f2 , end = ' ')
C(f1, f2, n, k)