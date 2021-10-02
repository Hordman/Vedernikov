"# -- coding: utf-8 --"
def D(n,m,k):
    if (k<n*m) and (k%n==0 or k%m==0):
        return "Да"
    else:
        return "Нет"
print(D(abs(int(input("n:"))),abs(int(input("m:"))),abs(int(input("k:"))))) 