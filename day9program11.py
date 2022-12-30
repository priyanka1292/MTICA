def printMonth(dn):
    mn=' '
    if(dn==1):
         mn='JANUARY'
    elif(dn==2):
        mn= 'FEBRUARY'
    elif(dn==3):
        mn= 'MARCH'
    elif(dn==4):
        mn= 'APRIL'
    elif(dn==5):
        mn='MAY'
    elif(dn==6):
        mn= 'JUNE'
    elif(dn==7):
        mn= 'JULY'
    elif(dn==8):
        mn= 'AUGUST'
    elif(dn==9):
        mn= 'SEPTEMBER'
    elif(dn==10):
        mn='OCTOBER'
    elif(dn==11):
         mn='NOVEMBER'
    elif(dn==12):
         mn='DECEMBER'
    else:
        mn='invalid'
    return mn

def printMonth1(dn):
    mn=' '
    if(dn==1):
         mn='JANUARY'
    if(dn==2):
        mn= 'FEBRUARY'
    if(dn==3):
        mn= 'MARCH'
    if(dn==4):
        mn= 'APRIL'
    if(dn==5):
        mn='MAY'
    if(dn==6):
        mn= 'JUNE'
    if(dn==7):
        mn= 'JULY'
    if(dn==8):
        mn= 'AUGUST'
    if(dn==9):
        mn= 'SEPTEMBER'
    if(dn==10):
        mn='OCTOBER'
    if(dn==11):
         mn='NOVEMBER'
    if(dn==12):
         mn='DECEMBER'
    return mn

import time
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(printMonth(inpNum))
    print((time.time()-start)*10000000)
    start=time.time()
    print(printMonth1(inpNum))
    print((time.time()-start)*10000000)
    
    

