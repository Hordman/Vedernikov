# -*- coding: utf-8 -*-
def D():
    K = int(input())
    v = 2
    t = 1
    while v <= K:
        v *= 2
        t += 1
    print( t - 1,  v // 2)
D()