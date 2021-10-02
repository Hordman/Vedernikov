"# -- coding: utf-8 --"
def D(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<= a and b<=c:
        return b
    else:
        return c
print(D(int(input("a:")),int(input("b:")),int(input("c:"))))   