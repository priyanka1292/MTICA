fo=open(r"E:\pythonpractice47\day10\dat10a.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")
