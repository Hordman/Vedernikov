#-*- coding: utf-8 -*-
a = int(input())
b = int(input())
def D (a,b):
	if a < b:
		print("Error")
	else:
		for K in range (a,b+1,-1):
			if K % 2 != 0:
				print(K)
D(a, b)