#-*- coding: utf-8 -*-
s = 'Какая-то  строка f с буквой f'
def K(s):
	if s.count('f') == 1:
		print(s.find('f'))
	elif s.count('f') >= 2:
		print(s.find('f'), s.rfind('f'))
K(s)