def addNumber(num1,num2):
    res=num1+num2
    return res
for i in range(3):
inp1=int(input("enter a no:"))
inp2=int(input("enter a no:"))
print(inp1,'+',inp2,'=',addNumber(inp1,inp2),sep='')
