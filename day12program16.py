class Rectangle:
    
    def __init__(self,width,length):
        assert(width>=0 and length>=0),"INVALID"
        self.width=width
        self.length=length
        
        
    def calculatePerimeter(self):
        temp=2*(self.length+self.width)
        return temp
       
    def calculateArea(self):
        temp=self.length*self.width
        return temp

w=int(input())
l=int(input())
try:
    rect=Rectangle(w,l)
    peri=rect.calculatePerimeter()
    area=rect.calculateArea()
    print('Area of rectangle is',area)
    print('Perimeter of rectangle is',peri)
except AssertionError as a:
    print(a)
   
