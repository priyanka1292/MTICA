import math
n=input()
total=0
for i in n:
    total+=math.pow(int(i),len(n))
if int(n)==total:
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number")
    
