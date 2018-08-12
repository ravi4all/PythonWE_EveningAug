Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = ["Ram", 30, "TCS", 25000.00]
>>> import numpy as np
>>> np.array(["Ram", 30, "TCS", 25000.00])
array(['Ram', '30', 'TCS', '25000.0'], dtype='<U7')
>>> data
['Ram', 30, 'TCS', 25000.0]
>>> data[0]
'Ram'
>>> data[2]
'TCS'
>>> data[-1]
25000.0
>>> data[-2]
'TCS'
>>> data.append("Delhi")
>>> data
['Ram', 30, 'TCS', 25000.0, 'Delhi']
>>> data.append(5)
>>> data
['Ram', 30, 'TCS', 25000.0, 'Delhi', 5]
>>> data = []
>>> data.append(5)
>>> data = []
>>> data.append(5)
>>> data
[5]
>>> data.append(10)
>>> data
[5, 10]
>>> data.append(15)
>>> data
[5, 10, 15]
>>> data = []
>>> for i in range(1,51):
	if i % 5 == 0:
		data.append(i)

		
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> "data is {}".format(data)
'data is [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]'
>>> data.pop()
50
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45]
>>> data.pop()
45
>>> data
[5, 10, 15, 20, 25, 30, 35, 40]
>>> data.append(45,50)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    data.append(45,50)
TypeError: append() takes exactly one argument (2 given)
>>> data.append(45)
>>> data.append(50)
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> 30 in data
True
>>> x = 30
>>> for i in range(len(data)):
	if x == data[i]:
		print("Data at {} index".format(i))

		
Data at 5 index
>>> data[5]
30
>>> table = [i for i in range(1,101) if i % 10 == 0]
>>> table
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> data.append(table)
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
>>> data.pop()
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> data.pop(5)
30
>>> data
[5, 10, 15, 20, 25, 35, 40, 45, 50]
>>> data.index(40)
6
>>> data.remove(0)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    data.remove(0)
ValueError: list.remove(x): x not in list
>>> data.remove(5)
>>> data
[10, 15, 20, 25, 35, 40, 45, 50]
>>> data.insert(0,5)
>>> data
[5, 10, 15, 20, 25, 35, 40, 45, 50]
>>> data.insert(5,30)
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> table
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> data.extend(table)
>>> data
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> data.count(10)
2
>>> data.index(10)
1
>>> for i in range(len(data)):
	if 10 == data[i]:
		print("Data at {} index".format(i))

		
Data at 1 index
Data at 10 index
>>> data.index(10,2)
10
>>> data.index(40)
7
>>> data.index(40,8)
13
>>> data.sort()
>>> data
[5, 10, 10, 15, 20, 20, 25, 30, 30, 35, 40, 40, 45, 50, 50, 60, 70, 80, 90, 100]
>>> data.sort(reverse = True)
>>> data
[100, 90, 80, 70, 60, 50, 50, 45, 40, 40, 35, 30, 30, 25, 20, 20, 15, 10, 10, 5]
>>> sorted(data)
[5, 10, 10, 15, 20, 20, 25, 30, 30, 35, 40, 40, 45, 50, 50, 60, 70, 80, 90, 100]
>>> sorted(data, reverse = True)
[100, 90, 80, 70, 60, 50, 50, 45, 40, 40, 35, 30, 30, 25, 20, 20, 15, 10, 10, 5]
>>> d = [4,7,9,3,4,7,0,1,2]
>>> sorted(d)
[0, 1, 2, 3, 4, 4, 7, 7, 9]
>>> d
[4, 7, 9, 3, 4, 7, 0, 1, 2]
>>> d.sort()
>>> d
[0, 1, 2, 3, 4, 4, 7, 7, 9]
>>> 
