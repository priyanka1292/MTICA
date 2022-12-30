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


for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
