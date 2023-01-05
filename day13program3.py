def PrintSunday():
    print("Sunday")
    return
def PrintMonday():
    print("Monday")
def PrintTuesday():
    print("Tuesday")
def PrintWednesday():
    print("Wednesday")
def PrintTursday():
    print("Thursday")
def PrintFriday():
    print("Friday")
def PrintSaturday():
    print("Saturday")
def Choice():
    print("0:Sunday")
    print("1:Monday")
    print("2:Tuesday")
    print("3:Wednesday")
    print("4:Thursday")
    print("5:Friday")
    print("6:Saturday")
    print("7:quit")
    return
daySelect={0:PrintSunday,1:PrintMonday,2:PrintTuesday,3:PrintWednesday,4:PrintTursday,
           5:PrintFriday,6:PrintSaturday}
Choice()
dayNum=int(input())
if dayNum>=1 and dayNum<=7:
    daySelect[dayNum] ()
else:
    print("INVALID")

    

    
