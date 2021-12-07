# -*- coding: utf-8 -*-
n= int (input())
K= 1
while n >> 1:
	K = K * n
	n = n - 1 
print (K)