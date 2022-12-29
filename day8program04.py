def  div(a,b):
     assert(b!=0),"factorial of negative number is not defined !"
     return a/b
     
try:
    print(div(55,0))
except Exception as obj:
    print(obj)
try:
    print(div(20,3))
except Exception as obj:
    print(obj)
try:
    print(div(100,20))
except Exception as obj:
    print(obj)
