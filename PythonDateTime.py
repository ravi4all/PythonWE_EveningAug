Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> choices = ["stone","paper","scissor"]
>>> random.choice(choices)
'scissor'
>>> random.choice(choices)
'scissor'
>>> random.choice(choices)
'scissor'
>>> random.choice(choices)
'paper'
>>> random.choice(choices)
'scissor'
>>> random.choice(choices)
'stone'
>>> random.choice(choices)
'scissor'
>>> random.choice(choices)
'scissor'
>>> random.choice(choices)
'stone'
>>> random.choice(choices)
'scissor'
>>> random.choice(choices)
'paper'
>>> random.choice(choices)
'paper'
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2018, 8, 5, 15, 25, 47, 273457)
>>> print(datetime.datetime.now().date())
2018-08-05
>>> print(datetime.datetime.now().time())
15:26:14.520260
>>> from datetime import datetime
>>> import webbrowser
>>> webbrowser.open("google.com")
True
>>> msg = "open google"
>>> msg.split()
['open', 'google']
>>> t = msg.split()
>>> t
['open', 'google']
>>> t[0]
'open'
>>> t[1]
'google'
>>> t[1] + ".com"
'google.com'
>>> datetime.now()
datetime.datetime(2018, 8, 5, 15, 46, 38, 116514)
>>> datetime.day
<attribute 'day' of 'datetime.date' objects>
>>> datetime.now().day
5
>>> datetime.today
<built-in method today of type object at 0x000000006E228510>
>>> datetime.today()
datetime.datetime(2018, 8, 5, 15, 47, 13, 295824)
>>> import calendar
>>> print(calendar.month(2018,8))
    August 2018
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

>>> datetime.now().weekday
<built-in method weekday of datetime.datetime object at 0x000001CBD22A50D0>
>>> datetime.now().weekday()
6
>>> datetime.now().date()
datetime.date(2018, 8, 5)
>>> d = datetime.now()
>>> d.date()
datetime.date(2018, 8, 5)
>>> d.weekday()
6
>>> datetime.now.strftime("%a %D %b %y")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    datetime.now.strftime("%a %D %b %y")
AttributeError: 'builtin_function_or_method' object has no attribute 'strftime'
>>> datetime.now().strftime("%a %D %b %y")
'Sun 08/05/18 Aug 18'
>>> datetime.now().strftime("%a")
'Sun'
>>> datetime.now().strftime("%D")
'08/05/18'
>>> datetime.now().strftime("%b")
'Aug'
>>> datetime.now().strftime("%y")
'18'
>>> datetime.now().strftime("%c")
'Sun Aug  5 15:51:57 2018'
>>> datetime.now().strftime("%I:%M:%S: %p")
'03:52:32: PM'
>>> 
