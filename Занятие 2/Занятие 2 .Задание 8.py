"# -- coding: utf-8 --"
def D(a,b,c):
    if a==b and a==c:
        return "3"
    elif a==b or a==c:
        return "2"
    else:
        return "0"
print(D(int(input("a:")),int(input("b:")),int(input("c:"))))   