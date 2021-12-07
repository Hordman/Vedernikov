# -- coding: utf-8 --
a=int(input())
b=int(input())
def D(a,b):
	
	if a<b:
		for K in range(a, b+1):
			print(K)
	else:
		for K in range(a,b-1,-1):
			print(K)
D(a,b)