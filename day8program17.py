def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpCh=input("enter a character:")
inpNum=int(input("enter a no:"))
printSeriesIncreasing(inpCh,inpNum)
print('-'*40)
printSeriesDecreasing(inpCh,inpNum)
