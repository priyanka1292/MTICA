def  factorial(num):
     assert(isinstance(num,int)),"factorial not defined for non integer"
     assert(num>=0),"factorial of negative number is not defined !"
     if num==0:
         return 1
     else:
        return num*factorial(num-1)
try:
    print(factorial(-45))
except Exception as obj:
    print(obj)
try:
    print(factorial(4.9))
except Exception as obj:
    print(obj)
try:
    print(factorial(45))
except Exception as obj:
    print(obj)
try:
    print(factorial('today'))
except Exception as obj:
    print(obj)
