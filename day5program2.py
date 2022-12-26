def checkPolindrome(inp):
    if inp==inp[::-1]:
        return 'yes'
    else:
        return 'no'
inp=input()
print(checkPolindrome(inp))
