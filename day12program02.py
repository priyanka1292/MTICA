def printPattern(n):
    assert(n>=0),'INVALID'
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end=' ')
            num+=1
    return None

inpnum=int(input())


try:
    printPattern(inpnum)
except AssertionError as obj:
    print(obj)
