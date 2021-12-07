# -*- coding: utf-8 -*-
def D():
    N = int(input())
    K = int(input())
    f = 0
    s = 1
    m = 0
    for i in range(2, N):
        c = s
        s = f + s
        f = c
        if(i >= K - 1 ):
            print(s)
            m += s
    print(m)
D()