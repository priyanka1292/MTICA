lst1=[11,22,33,44,55]
lst2=[1,2,3,4,5]
lst3=[5,6,5,2,1,3,2,3]#11*1+5

print(lst1)
print(lst2)
print(lst3)

ans=list(map(lambda a,b,c:a*b+c,lst1,lst2,lst3))
print(ans)






##lst1=[11,22,33,44,55]
##lst2=[1,2,3,4,5]
##ans=[]
###[12,24,37,48,60]
##def add(a,b):
##    return a+b
##
##ans=list(map(add,lst1,lst2))
##print(lst1)
##print(lst2)
##print(ans)
##
##print('-'*40)
##ans=list(map(lambda a,b:a+b,lst1,lst2))
##print(ans)
