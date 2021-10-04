"# -- coding: utf-8 --"
print("Введите время")
n=int(input())
h=0
m=0
h=n//60
m=n%60
if h>23:
    h=h%24
if m>59:
    m=m%60
print(h,"Часа")
print(m,"Минут")