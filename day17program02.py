from random import *
print(random())
print(randint(1,100))
print(uniform(1,10))
items=[1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)
x=sample(items,3)
print("x=",x)
print(x[0])
y=sample(items,4)
print(y)


##0.40298140475892186
##35
##3.567110624752481
##[1, 3, 4, 6, 9, 10, 5, 7, 8, 2]
##x= [8, 3, 2]
##8
##[6, 2, 1, 4]
