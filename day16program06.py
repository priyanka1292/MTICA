def printReverse(a):
   return [i[::-1] for i in a]
    
inp=input().strip().split()
print(*printReverse(inp))
