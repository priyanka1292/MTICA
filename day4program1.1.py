Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello' "world" 'python'
'helloworldpython'
a='hello' "world" 'python'
a
'helloworldpython'
type(a)
<class 'str'>
a=23,7.9,'python',a+bj,'c'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=23,7.9,'python',a+bj,'c'
NameError: name 'bj' is not defined
a=23,7.9,'python',1+2j,'c'
a
(23, 7.9, 'python', (1+2j), 'c')
type(a)
<class 'tuple'>
a=(5)
b=(5,)
type(a)
<class 'int'>
type(b)
<class 'tuple'>
a=(5.7)
b=(5.7,)
type(a)
<class 'float'>
type(b)
<class 'tuple'>
t=(23, 7.9, 'python', (1+2j), 'c')
type(t0
    )
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    type(t0
NameError: name 't0' is not defined. Did you mean: 't'?
type(t)
         
<class 'tuple'>
t=(23, 7.9, 'python', (1+2j), 'c',)
         
type(t)
         
<class 'tuple'>
t=[23, 7.9, 'python', (1+2j), 'c',]
         

t=[23, 7.9, 'python', (1+2j), 'c',]
         
type(t)
         
<class 'list'>
t={23, 7.9, 'python', (1+2j), 'c',}
         
type(t)
         
<class 'set'>
lst1=list()
         
type(lst1)
         
<class 'list'>
help(list)
         

lst1.append(10)
         
lst1.append(22.2)
         
lst1.append(15)
         
lst1.append('python')
         
lst1
         
[10, 22.2, 15, 'python']
lst1.clear()
         
lst1
         
[]
lst1=[10, 22.2, 15, 'python']
         
lst1.count(10)
         
1
lst1.count(15)
         
1
lst1.count(25)
         
0
lst1.append(10)
         
lst1
         
[10, 22.2, 15, 'python', 10]
lst1.count(10,1,5)
         
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    lst1.count(10,1,5)
TypeError: list.count() takes exactly one argument (3 given)
lst1.count(10,(1,5))
         
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    lst1.count(10,(1,5))
TypeError: list.count() takes exactly one argument (2 given)
lst1.count(10,(1,3))
         
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    lst1.count(10,(1,3))
TypeError: list.count() takes exactly one argument (2 given)
lst1.count(10,1,3)
         
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lst1.count(10,1,3)
TypeError: list.count() takes exactly one argument (3 given)
lst1
         
[10, 22.2, 15, 'python', 10]
lst1