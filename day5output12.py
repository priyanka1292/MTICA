#x=input('enter an integer==>')-->type error
x=int(input('enter an integer==>'))
y=x//10
z=y%10
#print(x,',',y,z) -->64 , 6 6
print(x,',',y,z,sep='') #64,66
#print(x,',',y,z,sep='@')-->64@,@6@6
#print(x,',',y,z,sep=' ')-->64 , 6 6
