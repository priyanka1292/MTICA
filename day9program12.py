def printDay(dn):
    if(dn==1):
        mn='MONDAY'
    elif(dn==2):
        mn= 'TUESDAY'
    elif(dn==3):
        mn='WEDNESDAY'
    elif(dn==4):
        mn= 'THURSDAY'
    elif(dn==5):
        mn='FRIDAY'
    elif(dn==6):
        mn= 'SATURDAY'
    elif(dn==7):
        mn='SUNDAY'
    else:
        mn= 'invalid'
    return mn

def printDay1(dn):
    if(dn==1):
        mn='MONDAY'
    if(dn==2):
        mn= 'TUESDAY'
    if(dn==3):
        mn='WEDNESDAY'
    if(dn==4):
        mn= 'THURSDAY'
    if(dn==5):
        mn='FRIDAY'
    if(dn==6):
        mn= 'SATURDAY'
    if(dn==7):
        mn='SUNDAY'
    return mn

import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print(time.time()-start)
    start=time.time()
    print(printDay1(inpNum))
    print(time.time()-start)


   
