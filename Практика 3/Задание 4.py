#-*- coding: utf-8 -*-
print("Введите число N")
N = int(input())
s = 0
def K(N, s):
	for i in range(N):
		s += int(input())
	print(s)

K(N, s)