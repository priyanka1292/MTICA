class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n +1):
            res *=i
        return res
    def checkEvenOdd(self):
        if self.n%2==0:
            return "Even"
        else:
            return "Odd"
    def sumOfDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for  i in temp:
            t+=int(i)
        return t
    def checkArmstrong(self):
        assert(self.n>=0),'INVALID'
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if t==self.n:
            return "Armstrong"
        else:
            return "Not Armstrong"
    def checkPrime(self):
        assert(self.n>=0),'INVALID'
        if self.n<=0:
            return "INVALID"
        
        if self.n==1 or self.n==2 or self.n==3:
            return "Prime"
        count=int(self.n//2)+1
        for i in range(2,count):
            if self.n%i==0:
                return 'Not Prime'
        return 'Prime'
        
inp=int(input())
obj=Number(inp)
print('Factorial of',inp,'is',obj.calculateFactorial())
print(inp,'is',obj.checkEvenOdd())
#print('Sum of Digits',inp,'is',obj.sumOfDigits())
try:
    print(inp,'is',obj.checkArmstrong())
    print(inp,'is',obj.checkPrime())
except AssertionError as a:
    print(a)
    

