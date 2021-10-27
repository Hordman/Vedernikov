#-*- coding: utf-8 -*-
s = 'Строка для задания'
def K(s):
	a = (s[len(s) // 2:] + s[:len(s) // 2])
	print(a)
K(s)
