#count the number of space in a given string.Do not use string function and use list comprehension 
##string='''practice problems for list comprehension in python'''
##ans=[]
##for i in string:
##    if i==' ':
##        ans.append(i)
##print(len(ans))
#print(string.count(' '))

string='''practice problems for list comprehension in python'''
ans=[ i  for i in string  if i ==' ']
print(len(ans))
