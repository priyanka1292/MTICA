def checkEven(num1):
    if num1%2==0:
        return "even"
    return None
    
def checkOdd(num1):
    if num1%2==1:
       return "odd"
    return None

num=int(input("enter a n0:"))
x=checkEven(num)
y=checkOdd(num)

print("x=",x)
print("y=",y)

print(checkEven(num))
print(checkOdd(num))
