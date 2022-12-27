#remove all the vowel in the given string


##string='''practice problem for list comprehension in py?hn'''
##ans=[]
##for i in string:
##    if i not in 'AEIOUaeiou':
##        ans.append(i)
##print(*ans)


string='''practice problem for list comprehension in py?hn'''
ans=[ i for i in string if i not in 'AEIOUaeiou' ]
print(*ans)
