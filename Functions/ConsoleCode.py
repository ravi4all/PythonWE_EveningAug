Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def calc(x,y):
	return x + y, x - y, x / y, x * y

>>> calc(10,12)
(22, -2, 0.8333333333333334, 120)
>>> a,b,c,d = calc(10,12)
>>> a1 = calc(10,12)
>>> a
22
>>> b
-2
>>> c
0.8333333333333334
>>> d
120
>>> a1
(22, -2, 0.8333333333333334, 120)
>>> calc(10,12)[1]
-2
>>> def calc():
	return lambda x,y : x + y

>>> calc()
<function calc.<locals>.<lambda> at 0x00000257803626A8>
>>> x = calc()
>>> x(10,12)
22
>>> a = lambda x,y : x + y
>>> a
<function <lambda> at 0x00000257803626A8>
>>> a()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a()
TypeError: <lambda>() missing 2 required positional arguments: 'x' and 'y'
>>> a(10,12)
22
>>> data = [['Ram',78],['Aman',65],['Shyam',45],['Kamal',67]]
>>> sorted(data)
[['Aman', 65], ['Kamal', 67], ['Ram', 78], ['Shyam', 45]]
>>> sorted(data, key=lambda x : x[1])
[['Shyam', 45], ['Aman', 65], ['Kamal', 67], ['Ram', 78]]
>>> sorted(data, key=lambda x : x[1], reversed = True)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    sorted(data, key=lambda x : x[1], reversed = True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> sorted(data, key=lambda x : x[1], reverse = True)
[['Ram', 78], ['Kamal', 67], ['Aman', 65], ['Shyam', 45]]
>>> 
