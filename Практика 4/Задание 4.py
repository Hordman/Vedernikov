#-*- coding: utf-8 -*-
s = 'Какая-то строка'
def K(s):
	f = s[:s.find(' ')]
	sc = s[s.find(' ') + 1:]
	print(sc + ' ' + f)
K(s)