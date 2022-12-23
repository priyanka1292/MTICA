def checkEven(n):
    if n<0:
        return "invalid"
    n=str(n)
    if n[-1] in '02468':
        return "even"
    if n[-1] in '13579':
        return "odd"
inpNum=int(input())
print(checkEven(inpNum))
