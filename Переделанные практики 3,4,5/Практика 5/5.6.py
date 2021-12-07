# -- coding: utf-8 --
def D():
    K=int(input())
    S=0
    Z=0
    while K!=0:
        Z+=K
        S+=1
        K=int(input())
    print(Z/S)
print(D())