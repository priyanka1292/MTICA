Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=set()
type(a)
<class 'set'>
b={3}
type(b)
<class 'set'>
c={'mansa','prasad','manohar','ganguly'}
type(c)
<class 'set'>
d={}
type(d)
<class 'dict'>
a={1,2,3,4,5,6}
b={4,5,6,7,8}
a.intersection(b)
{4, 5, 6}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
s='today is monday'
a=list(s)
a
['t', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'm', 'o', 'n', 'd', 'a', 'y']
set(a)
{'s', 't', 'y', 'm', 'o', 'a', 'i', ' ', 'd', 'n'}
a={11,22,33,44,55,11,66,77,33}
b=list(set(a))
b
[33, 66, 22, 55, 11, 44, 77]
