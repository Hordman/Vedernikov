#-*- coding: utf-8 -*-
print("Введите числа A и B, где A =< B")
a = int(input())
b = int(input())
def K(a, b):
	if a > b:
		print('Ошибка')
	else:
		for i in range(a, b + 1):
			print(i)
			i += 1
K(a, b)