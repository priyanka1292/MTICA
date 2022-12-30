def printMonth(dn):
    if(dn==1):
        return 'JANUARY'
    elif(dn==2):
        return 'FEBRUARY'
    elif(dn==3):
        return 'MARCH'
    elif(dn==4):
        return 'APRIL'
    elif(dn==5):
        return 'MAY'
    elif(dn==6):
        return 'JUNE'
    elif(dn==7):
        return 'JULY'
    elif(dn==8):
        return 'AUGUST'
    elif(dn==9):
        return 'SEPTEMBER'
    elif(dn==10):
        return 'OCTOBER'
    elif(dn==11):
        return 'NOVEMBER'
    elif(dn==12):
        return 'DECEMBER'
    else:
        return 'invalid'
    



for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
