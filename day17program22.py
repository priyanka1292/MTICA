##def removespecialchar(ch):
##    s=[]
##    for i in ch:
##        if i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
##            s.append(i)
##    return s
##inp=input()
##print(*removespecialchar(inp),sep='')



def removespecialchar(ch):
    s=[]
    for i in ch:
        if(ord(i) in range(65,90) or ord(i) in range(97,123) or ord(i) in range(48,56)):
            s+=i
    return s
inp=input()
print(*removespecialchar(inp),sep='')
