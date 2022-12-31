fo1=open(r'E:\pythonpractice47\day10\dat10a.txt',"r")
fo2=open(r'E:\pythonpractice47\day10\test.txt',"w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File Copied")
