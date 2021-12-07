# -*- coding: utf-8 -*-
n= int (input())
k= 1
s= 0
for d in range(1, n + 1):
    k *= d
    s += k
print(s)