'''
write a program to find list of factor of a numbers.
Factor is the integer that can exactly divide
a given number without leaving a remainder'''


def findFactor(n):
   temp=list()
   for i in range(1,n+1):
       if n%i==0:
           temp.append(i)
   return temp

num=int(input())
print(*findFactor(num))
