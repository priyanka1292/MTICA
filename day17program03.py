import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i==0:
        print("function name :{0}".format(sys.argv[0]))
        #print("function name: %s" % sys.argv[0])
    else:
        print("{0}.argument:{1}".format(i,sys.argv[i]))
        #print("%d. argument:%s" %(i,sys.argv[i]))



#command prompt
##D:\pythonpractice25\day17>python day17program03.py priyanka ayeesha mca mtica
##['day17program03.py', 'priyanka', 'ayeesha', 'mca', 'mtica']
##function name :day17program03.py
##1.argument:priyanka
##2.argument:ayeesha
##3.argument:mca
##4.argument:mtica
