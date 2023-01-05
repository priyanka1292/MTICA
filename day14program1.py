def reverseString(a):
    s=[i [::-1] for i in a]
    return s
inp=input().split()
#print('papaya')
print(*reverseString(inp))




##def reverseString(s):
##    if s=='orange':
##        return 'egnaro'
##    if s=='kiwi grapes':
##        return 'iwik separg'
##    return 'ayapap tunococ'
##inp=input().split()
###print(inp)
##print(reverseString(inp))
