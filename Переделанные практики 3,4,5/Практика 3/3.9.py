# -*- coding: utf-8 -*-
f1 = f2 = 1
n = int(input())
fK = f1+f2
while n > 0:
    f1,f2 = f2, f1+f2
    n-=1
    fK += f2
print(fK)