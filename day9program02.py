def printSeriesIncreasing(ch,n):
    assert isinstance(ch,str),"First argument should be string"
    assert isinstance(n,int),"Second argument should be int"
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),"First argument should be string"
    assert isinstance(n,int),"Second argument should be int" 
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpCh=input("enter a character:")
inpNum=int(input("enter a number:"))
try:
    printSeriesIncreasing(inpCh,inpNum)
except AssertionError as obj:
    print(obj)
print('-'*40)
try:
    printSeriesDecreasing(inpCh,inpNum)
except AssertionError as obj:
    print(obj)
