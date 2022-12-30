fo=open(r"E:\pythonpractice47\day9\abc2.txt","w+")
inpstr=input("Enter text:")
fo.write(inpstr)
inpstr=input("Enter text:")
fo.write(inpstr)

fo.close()
print('Text Written to File')
