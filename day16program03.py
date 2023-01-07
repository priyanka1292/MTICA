'''WAP to remove special character from a string.
Any character excluding alphabet and digits are special character.
output should be string without any special character.


Example:
INPUT:
 fun_Add()
OUTPUT:
 funAdd

INPUT:
  praven.nsic1@gmail.com
OUTPUT:
  pravennsic1gmailcom

INPUT:
 -786.56
OUTPUT:
 78656

'''
def removeSpecialChar(s):
    ans=''
    for i in s:
        if (ord(i) in range(65,91) or ord(i) in range(97,123)
        or ord(i) in range(48,57)):
            #ans+=i
            ans.append(i)

    #return ans
    return ''.join(ans)
    
    

inp=input()
print(removeSpecialChar(inp))


##def removeSpecialChar(s):
##    ans=[]
##    for i in s:
##        if i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
##            ans.append(i)
##    return ''.join(ans)
##    
##    
##
##inp=input()
##print(removeSpecialChar(inp))
