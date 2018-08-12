Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> sent = "hello this is python programming"
>>> sent[0]
'h'
>>> sent[5]
' '
>>> sent[0:5]
'hello'
>>> sent[13]
' '
>>> sent[14]
'p'
>>> sent[14:20]
'python'
>>> sent[-1]
'g'
>>> sent[-4]
'm'
>>> len(sent)
32
>>> sent
'hello this is python programming'
>>> sent[0:30:2]
'hloti spto rgam'
>>> sent[0:30:3]
'hltssyopgm'
>>> dir(sent)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> sent.count('i')
3
>>> sent.upper()
'HELLO THIS IS PYTHON PROGRAMMING'
>>> sent.index('p')
14
>>> sent.replace('hello','bye')
'bye this is python programming'
>>> sent
'hello this is python programming'
>>> sent.split()
['hello', 'this', 'is', 'python', 'programming']
>>> sent.find('p')
14
>>> sent
'hello this is python programming'
>>> sent.index('p',15)
21
>>> se
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    se
NameError: name 'se' is not defined
>>> sent.rfind('i')
29
>>> sent.index('p')
14
>>> sent.index('n',15)
19
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/PythonWE_Evening/01-Python/PrintStrinfs.py 
Enter first name : Ram
Enter last name : Sharma
Hello Ram Sharma
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/PythonWE_Evening/01-Python/PrintStrinfs.py 
Enter first name : RaM
Enter last name : shARma
Hello RaM shARma
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/PythonWE_Evening/01-Python/PrintStrinfs.py 
Enter first name : RAM
Enter last name : sharMA
Hello ram sharma
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/PythonWE_Evening/01-Python/PrintStrinfs.py 
Enter first name : ram
Enter last name : shARMa
Hello RAM SHarmA
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/PythonWE_Evening/01-Python/PrintStrinfs.py 
Enter first name : RAm
Enter last name : ShaRMA
Hello RAM SHARMA
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/PythonWE_Evening/01-Python/PrintStrinfs.py 
Enter first name : ram
Enter last name : SharMA
Hello RAM SHARMA
>>> firstname
'ram'
>>> firstname[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    firstname[0] = 'a'
TypeError: 'str' object does not support item assignment
>>> firstname.replace('r','a')
'aam'
>>> firstname
'ram'
>>> firstname = firstname.replace('r','a')
>>> firstname
'aam'
>>> 
