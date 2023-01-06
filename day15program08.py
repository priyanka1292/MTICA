'''write a program to calculate GCD of two numbers.
the HCF or GCD of two positive integers  is nothing as input and output
'''

def findFactor(n):
   temp=list()
   for i in range(1,n+1):
       if n%i==0:
           temp.append(i)
   return temp


def findGCD(n1,n2):
    lstn1=findFactor(n1)
    lstn2=findFactor(n2)
    s1=set(lstn1)
    s2=set(lstn2)
    a=list(s1.intersection(s2))
    a.sort()
    return a[-1]
print("enter two number")
a=int(input())
b=int(input())
print(findGCD(a,b))   
    
