Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random as r
r.random()
0.3732166550957172
help(r.random)
Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).

r.randint(1,100)
57
help(r.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help(r.uniform)
Help on method uniform in module random:

uniform(a, b) method of random.Random instance
    Get a random number in the range [a, b) or [a, b] depending on rounding.

r.uniform(10,100)
24.190685192276792
i