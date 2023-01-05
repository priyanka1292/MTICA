Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: E:/pythonpractice47/day14/day14program16.py =============
pt1=Point()
pt1=Point(1,2)
Point destroyed
pt2=pt1
pt3=pt1
print(id(pt1),id(pt2),id(pt3))
1610016593616 1610016593616 1610016593616
del pt1
del pt2
del pt3
Point destroyed
pt11=Point(6,7)
del pt11
Point destroyed
