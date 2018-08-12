Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup = 10,
>>> type(tup)
<class 'tuple'>
>>> tup
(10,)
>>> tup = 10,20,30,40
>>> tup
(10, 20, 30, 40)
>>> tup = (10,20,30,40)
>>> tup
(10, 20, 30, 40)
>>> tup[0] = 100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tup[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> emp = name, company, salary = "Ram", "HCL", 24000
>>> emp
('Ram', 'HCL', 24000)
>>> name
'Ram'
>>> company
'HCL'
>>> dalary
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    dalary
NameError: name 'dalary' is not defined
>>> salary
24000
>>> emp
('Ram', 'HCL', 24000)
>>> 
