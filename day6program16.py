#remove all the vowel in the given string


string='''practice problem for list comprehension in python'''
##ans=[]
##for i in string:
##    if i not in 'AEIOUaeiou':
##        ans.append(i)
##print(*ans)


##string='''practice problem for list comprehension in python'''
##ans=[ i for i in string if i not in 'AEIOUaeiou' ]
##print(*ans)




ans=[i for i in string if i not in 'AEIOUaeiou']
print(''.join(ans))
