def  fact(n):
     assert(n>=0),"factorial of negative number is not defined !"
     if n==0:
         return 1
     else:
        return n*fact(n-1)
try:
    print(fact(-45))
except Exception as ob:
    print(ob)
try:
    print(fact(45))
except Exception as ob:
    print(ob)
##try:
##    print(fact(0))
##except Exception as ob:
##    print(ob)
##
##
##print("Thank You")
##
##
