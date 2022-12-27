Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir(builtins)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dir(builtins)
NameError: name 'builtins' is not defined
import math
dir(math)

import builtins
dir(builtins)


================================ RESTART: Shell ================================
import math
math.sqrt(2)
1.4142135623730951

================================ RESTART: Shell ================================
from math import sqrt
sqrt(2)
1.4142135623730951
sqrt(9)
3.0
gcd(24,40)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    gcd(24,40)
NameError: name 'gcd' is not defined

================================ RESTART: Shell ================================
from math import *
sqrt(9)
3.0
gcd(24,40)
8

============================================ RESTART: Shell ============================================
import mathsqrtmath.sqrt(2)
SyntaxError: invalid syntax
import mathsqrtmath.sqrt(2)
SyntaxError: invalid syntax
import math
math.sqrt(2)
1.4142135623730951

============================================ RESTART: Shell ============================================
from math import sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(24,40)
8

============================================ RESTART: Shell ============================================
import math as m
m.sqrt(3)
1.7320508075688772
m.gcd(24,40)
8
m.tan(30)
-6.405331196646276
m.gcd(2,4)
2

============================================ RESTART: Shell ============================================
import math
gcd(2,4)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    gcd(2,4)
NameError: name 'gcd' is not defined
from math import *
gcd(2,4)
2

============================================ RESTART: Shell ============================================

============================================ RESTART: Shell ============================================
import math as m
m.trunc(4.5)
4
m.floor(4.5)
4
m.ceil(4.5)
5
m.trunc(9.1)
9
m.log(1024,2)
10.0
m.log(1024,10)
3.0102999566398116
abs(-3.5)
3.5
hex(3)
'0x3'

============================================ RESTART: Shell ============================================
print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
apple,banana,carrot
print('{0},{1}{0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,bananaappleapplepen carrot
print('{0},{1} {0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana appleapplepen carrot
print('{0},{1} {0},{0} {3} {2}'.format('apple','banana','carrot','pen'))
apple,banana apple,apple pen carrot
print('{0},{1},{0},{0},{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana,apple,apple,pen carrot
print('{},{},{}'.format('apple','banana','carrot'))
apple,banana,carrot
print('priyanka purchased a kg of {},a dozen of {} and half kg of {}'.format('apple','banana','carrot'))
priyanka purchased a kg of apple,a dozen of banana and half kg of carrot
print('{},{},{}'.format('apple','banana','carrot','pen'))
apple,banana,carrot
print('priyanka purchased a kg of {0} and {3},a dozen of {1} and half kg of {1}'.format('apple','banana','carrot'))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print('priyanka purchased a kg of {0} and {3},a dozen of {1} and half kg of {1}'.format('apple','banana','carrot'))
IndexError: Replacement index 3 out of range for positional args tuple
print('priyanka purchased a kg of {0} and {2},a dozen of {1} and half kg of {1}'.format('apple','banana','carrot'))
priyanka purchased a kg of apple and carrot,a dozen of banana and half kg of banana
print('{2},{1},{0}'.format(*'abcd'))
c,b,a
x,*y,z='computer'
x
'c'
y
['o', 'm', 'p', 'u', 't', 'e']
z
'r'
*x,y='abcd'
x
['a', 'b', 'c']
y
'd'
 '{2},{1},{0}'.format(*'abcd')
 
SyntaxError: unexpected indent
('{2},{1},{0}'.format(*'abcd'))
'c,b,a'
print('coordinates: {latitude},{longitude}'.format(latitude='37.2N',longitude='-115.81W'))
coordinates: 37.2N,-115.81W
print('Welcome:{name},your college is: {college}'.format(name='Priyanka',college='MTICA'))
Welcome:Priyanka,your college is: MTICA

============================================ RESTART: Shell ============================================

coord={'latitude':'37.25N','longitude':'-115.81W}
       
SyntaxError: unterminated string literal (detected at line 1)
coord={'latitude':'37.25N','longitude':'-115.81W'}
       
