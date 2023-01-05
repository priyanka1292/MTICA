#dictionary as switch
def PrintBlue():
    print('you chose blue!\n')
    return
def PrintRed():
    print('you chose red!\n')
def PrintOrange():
    print('you chose orange!\n')
def PrintGreen():
    print('you chose green!\n')
def Choice():
    print("1:Blue")
    print("2:Red")
    print("3:Orange")
    print("4:Green")
    print("5:Quit")
    return
colorSelect={1:PrintBlue, 2:PrintRed(), 3:PrintOrange(), 4:PrintGreen()}
selection=0
while True:
    if selection==4:
        break
    Choice()
    selection=int(input("select a color option:"))
    if(selection>=0)and(selection<4):
        colorSelect[selection]()
