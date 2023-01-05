'''print length of a string
input:mango
otput:5'''


def printFruit(s):
    lst=s.split()
    return [len(i) for i in lst]

inp=input()
print(*printFruit(inp))
    






                                                                    
