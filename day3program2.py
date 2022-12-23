import math
def checkPrimeNumber(num):
    if num<1:
        return 0
    if num==1:
        return num
    count=int(math.sqrt(num))+1
    for i in range(2,count):
        if num%i==0:
            return 0
    return num
inpNum=int(input("enter a number:"))
if checkPrimeNumber(inpNum):
    print(inpNum," is a prime number");
else:
    print(inpNum,"not a prime number");
    
