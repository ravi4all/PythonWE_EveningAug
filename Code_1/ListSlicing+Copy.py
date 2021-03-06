Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = [[2,4,6,8,10],[5,10,15,20,25],[10,20,30,40,50]]
>>> data[0]
[2, 4, 6, 8, 10]
>>> data[0].append(12)
>>> data
[[2, 4, 6, 8, 10, 12], [5, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> x = data[0]
>>> data[1].append(30)
>>> data[2].append(60)
>>> data
[[2, 4, 6, 8, 10, 12], [5, 10, 15, 20, 25, 30], [10, 20, 30, 40, 50, 60]]
>>> data[0][3]
8
>>> data = [2, 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> data
[2, 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> data[0:8]
[2, 4, 6, 8, 10, 12, 5, 10]
>>> data[8:20]
[15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> data[8:]
[15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> len(data)
18
>>> data[0:16:2]
[2, 6, 10, 5, 15, 25, 10, 30]
>>> a = data
>>> a
[2, 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> data
[2, 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> id(data)
2457552391560
>>> id(a)
2457552391560
>>> data[0] = "hello"
>>> data
['hello', 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> a
['hello', 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> b = data[:]
>>> b
['hello', 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> a
['hello', 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> data
['hello', 4, 6, 8, 10, 12, 5, 10, 15, 20, 25, 30, 10, 20, 30, 40, 50, 60]
>>> id(data)
2457552391560
>>> id(a)
2457552391560
>>> id(b)
2457512173256
>>> a == data
True
>>> a is data
True
>>> a == b
True
>>> a is b
False
>>> data = [[2,4,6,8,10],[5,10,15,20,25],[10,20,30,40,50]]
>>> data
[[2, 4, 6, 8, 10], [5, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> a = data[:]
>>> a
[[2, 4, 6, 8, 10], [5, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> data
[[2, 4, 6, 8, 10], [5, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> a is data
False
>>> data[0] = "bye"
>>> data
['bye', [5, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> a
[[2, 4, 6, 8, 10], [5, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> data[1][0] = 0
>>> data
['bye', [0, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> a
[[2, 4, 6, 8, 10], [0, 10, 15, 20, 25], [10, 20, 30, 40, 50]]
>>> data = [2,3,4,6,7,[10,20,30,40,50]]
>>> a = data[:]
>>> a
[2, 3, 4, 6, 7, [10, 20, 30, 40, 50]]
>>> data
[2, 3, 4, 6, 7, [10, 20, 30, 40, 50]]
>>> data[0] = 0
>>> data
[0, 3, 4, 6, 7, [10, 20, 30, 40, 50]]
>>> a
[2, 3, 4, 6, 7, [10, 20, 30, 40, 50]]
>>> data[-1][0] = 100
>>> data
[0, 3, 4, 6, 7, [100, 20, 30, 40, 50]]
>>> a
[2, 3, 4, 6, 7, [100, 20, 30, 40, 50]]
>>> import copy
>>> b = copy.deepcopy(data)
>>> b
[0, 3, 4, 6, 7, [100, 20, 30, 40, 50]]
>>> data
[0, 3, 4, 6, 7, [100, 20, 30, 40, 50]]
>>> data[-1][0] = 10
>>> data
[0, 3, 4, 6, 7, [10, 20, 30, 40, 50]]
>>> a
[2, 3, 4, 6, 7, [10, 20, 30, 40, 50]]
>>> b
[0, 3, 4, 6, 7, [100, 20, 30, 40, 50]]
>>> 
