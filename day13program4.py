def PrintAdd(a,b):
    print(a+b)
def PrintMul(a,b):
    print(a*b)
def PrintSub(a,b):
    print(a-b)
def PrintDiv(a,b):
    print(a/b)
def choice():
    print("+:Addition");
    print("*:Multiplication");
    print("-:subtraction");
    print("/:Division");
    print("q:Quit");
    return
ArithmeticSelect={"+":PrintAdd,"-":PrintSub,"*":PrintMul,"/":PrintDiv}
while True:
    choice()
    selection=input("select an Arithmetic operation: ")
    if(selection=='q' or selection=='Q'):break
    if((selection=='+') or (selection=='-') or 
          (selection=='*') or (selection=='/')):
          n1=int(input("enter first num:"))
          n2=int(input("enter second num:"))
          z=ArithmeticSelect[selection](n1,n2)
          print(n1,selection,n2,'=',z)

    
