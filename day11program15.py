##def printPattern(ch,n):
##    for i in range(n+1):
##        print(ch*i)
##ch=input()
##n=int(input())
####printPattern(ch,n)
##
##
##def printPattern(ch,n):
##    assert(n>=0),'INVALID'
##    for i in range(n):
##        print(ch*i)
##ch=input()
##n=int(input())
##
##try:
##    printPattern(ch,n)
##except AssertionError as a:
##    print(a)
##
##
def printPattern(ch,n):
    assert(n>=0),'INVALID'
    for i in range(n,0,-1):
        print(ch*i)
ch=input()
n=int(input())

try:
    printPattern(ch,n)
except AssertionError as a:
    print(a)

