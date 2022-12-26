def sumDigits(n):
    n=str(n)
    total=0
    for i in n:
        total+=int(n)
    return total

n=int(input("enter a number"))
count=len(str(sumDigit(n))
while(count!=1):
    n=sumDigit(n)
    count+=len(str(sumDigit(n)))
print(n)
