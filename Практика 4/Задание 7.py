#-*- coding: utf-8 -*-
s = 'строка h с буквой h'
def K(s):	
	s = s[:s.find('h')] + s[s.rfind('h') + 1:]
	print(s)
K(s)
