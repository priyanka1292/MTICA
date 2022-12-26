inpArea=int(input("enter area of circle:"))
if inpArea<0:
    print("invalid area")
else:
    pi=3.14159
    radius=round((inpArea/pi)**(1/2),6)
    print("for the given area",inpArea,"radius is:",radius)
    print("area:"+str(inpArea),"radius:"+str(radius))
