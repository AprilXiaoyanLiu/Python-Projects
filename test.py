Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pandas
ImportError: No module named pandas
>>> st_list = [['a','b','c'],['d','a','e'],['a','b','f']]
>>> imp_list = [5,7,9]
>>> impr = [(k,v) for k in (for i in st_list) for v in imp_list]
SyntaxError: invalid syntax
>>> impr = [(k,v) for i in st_list for v in imp_list]

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    impr = [(k,v) for i in st_list for v in imp_list]
NameError: name 'k' is not defined
>>> impr = [(k,v) for k in st_list for v in imp_list]
>>> print impr
[(['a', 'b', 'c'], 5), (['a', 'b', 'c'], 7), (['a', 'b', 'c'], 9), (['d', 'a', 'e'], 5), (['d', 'a', 'e'], 7), (['d', 'a', 'e'], 9), (['a', 'b', 'f'], 5), (['a', 'b', 'f'], 7), (['a', 'b', 'f'], 9)]
>>> frequency = {}
>>> for i in st_list:
	i = i.split()
	if i not in frequency:
		frequency[i] = 1
	elif i in frequency:
		frequency [i] += 1

		

Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    i = i.split()
AttributeError: 'list' object has no attribute 'split'
>>> for m in st_list:
	for i in m:
		i = i.split()
		if i not in frequency:
			frequency[i] = 1
		elif i in frequency:
			frequency [i] += 1

			

Traceback (most recent call last):
  File "<pyshell#16>", line 4, in <module>
    if i not in frequency:
TypeError: unhashable type: 'list'
>>> for m in st_list:
	for i in m:
		print i

		
a
b
c
d
a
e
a
b
f
>>> type(i)
<type 'str'>
>>> for m in st_list:
	for i in m:
		i = i.split()
		if i not in frequency:
			frequency[i] = 1
		elif i in frequency:
			frequency[i] += 1

			

Traceback (most recent call last):
  File "<pyshell#29>", line 4, in <module>
    if i not in frequency:
TypeError: unhashable type: 'list'
>>> 
>>> for m in st_list:
	print m

	
['a', 'b', 'c']
['d', 'a', 'e']
['a', 'b', 'f']
>>> 
======================== RESTART: C:/Python27/test.py ========================
>>> 
======================== RESTART: C:/Python27/test.py ========================
>>> st_list = [['a','b','c'],['d','a','e'],['a','b','f']]
>>> imp_list = [5,7,9]
>>> fre = {}
>>> for m in st_list:
	for i in m:
		if i in fre:
			fre[i] += 1
		elif i not in fre:
			fre[i] = 1

			
>>> print fre
{'a': 3, 'c': 1, 'b': 2, 'e': 1, 'd': 1, 'f': 1}
>>> total_imp = {}
>>> test = [(k[i],v) for i in enumerate(for k in st_list) for v in imp_list]
SyntaxError: invalid syntax
>>> test_list = [['a','b','c'],['d','a','e','g'],['a','b','f']]
>>> t = [(i,j) for i, j in enumerate(test_list)]
>>> t
[(0, ['a', 'b', 'c']), (1, ['d', 'a', 'e', 'g']), (2, ['a', 'b', 'f'])]
>>> t = [(i,j) for i, j in enumerate([m, for m in st_list])]
SyntaxError: invalid syntax
>>> test = [(k[i],v) for i in enumerate([k for k in st_list]) for v in imp_list]

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    test = [(k[i],v) for i in enumerate([k for k in st_list]) for v in imp_list]
TypeError: list indices must be integers, not tuple
>>> test1 = [(k,v) for k in st_list for v in imp_list]
>>> test1
[(['a', 'b', 'c'], 5), (['a', 'b', 'c'], 7), (['a', 'b', 'c'], 9), (['d', 'a', 'e'], 5), (['d', 'a', 'e'], 7), (['d', 'a', 'e'], 9), (['a', 'b', 'f'], 5), (['a', 'b', 'f'], 7), (['a', 'b', 'f'], 9)]
>>> for j in test1:
	print j

	
(['a', 'b', 'c'], 5)
(['a', 'b', 'c'], 7)
(['a', 'b', 'c'], 9)
(['d', 'a', 'e'], 5)
(['d', 'a', 'e'], 7)
(['d', 'a', 'e'], 9)
(['a', 'b', 'f'], 5)
(['a', 'b', 'f'], 7)
(['a', 'b', 'f'], 9)
>>> test1 = [[k,v] for k in st_list for v in imp_list]
>>> test1
[[['a', 'b', 'c'], 5], [['a', 'b', 'c'], 7], [['a', 'b', 'c'], 9], [['d', 'a', 'e'], 5], [['d', 'a', 'e'], 7], [['d', 'a', 'e'], 9], [['a', 'b', 'f'], 5], [['a', 'b', 'f'], 7], [['a', 'b', 'f'], 9]]
>>> for j in test1:
	print j

	
[['a', 'b', 'c'], 5]
[['a', 'b', 'c'], 7]
[['a', 'b', 'c'], 9]
[['d', 'a', 'e'], 5]
[['d', 'a', 'e'], 7]
[['d', 'a', 'e'], 9]
[['a', 'b', 'f'], 5]
[['a', 'b', 'f'], 7]
[['a', 'b', 'f'], 9]
>>> for j in test1:
	print j[0]

	
['a', 'b', 'c']
['a', 'b', 'c']
['a', 'b', 'c']
['d', 'a', 'e']
['d', 'a', 'e']
['d', 'a', 'e']
['a', 'b', 'f']
['a', 'b', 'f']
['a', 'b', 'f']
>>> t1 = ['a','b','c']
>>> t2 = [5]
>>> t3 = [i:j for i in t1 for j in t2]
SyntaxError: invalid syntax
>>> t2 = [(i,j) for i in t1 for j in t2]
>>> t2
[('a', 5), ('b', 5), ('c', 5)]
>>> t1 = [['a','b','c']]
>>> t2 = 5
>>> t3 = [(i,j) for i in t1 for j in t2]

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t3 = [(i,j) for i in t1 for j in t2]
TypeError: 'int' object is not iterable
>>> t2 = [5]
>>> t3 = [(i,j) for i in t1 for j in t2]
>>> t3
[(['a', 'b', 'c'], 5)]
>>> st_list = [['a','b','c'],['d','a','e'],['a','b','f']]
>>> imp_list = [5,7,9]
>>> for i in st_list:
	t3 = [(a,b) for a in i for b in imp_list]

	
>>> t3
[('a', 5), ('a', 7), ('a', 9), ('b', 5), ('b', 7), ('b', 9), ('f', 5), ('f', 7), ('f', 9)]
>>> for i in range(len(st_list)):
	t3 = [(a,imp_list[i]) for a in st_list[i]]

	
>>> t3
[('a', 9), ('b', 9), ('f', 9)]
>>> st_list = [['a','b','c'],['d','a','e'],['a','b','f']]
>>> imp_list = [5,7,9]
>>> for x in range(len(st_list)):
	t5 = [(a,imp_list[i]) for a in st_list[i]]
	print t5

	
[('a', 9), ('b', 9), ('f', 9)]
[('a', 9), ('b', 9), ('f', 9)]
[('a', 9), ('b', 9), ('f', 9)]
>>> st_list = [['a','b','c'],['d','a','e'],['a','b','f']]
>>> imp_list = [5,7,9]
>>> new_list = []
>>> for i in range(len(st_list)):
	for a in st_list[i]:
		print a

		
a
b
c
d
a
e
a
b
f
>>> for i in range(len(st_list)):
	for a in st_list[i]:
		new_list.append(a,imp_list[i])

		

Traceback (most recent call last):
  File "<pyshell#99>", line 3, in <module>
    new_list.append(a,imp_list[i])
TypeError: append() takes exactly one argument (2 given)
>>> new_list.tuple()

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    new_list.tuple()
AttributeError: 'list' object has no attribute 'tuple'
>>> y.tuple()

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    y.tuple()
NameError: name 'y' is not defined
>>> t = tuple()
>>> for i in range(len(st_list)):
	for a in st_list[i]:
		t.append(a,imp_list[i])

		

Traceback (most recent call last):
  File "<pyshell#105>", line 3, in <module>
    t.append(a,imp_list[i])
AttributeError: 'tuple' object has no attribute 'append'
>>> 
