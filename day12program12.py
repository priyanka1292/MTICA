class Student:
    college='MTICA'  
    course='MCA'
               
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def displayStudent(self):
       print('Name :  '+self.name.title())
       print('Rollno :'+str(self.rollno))
       print('College :  '+self.college)
       print('Course : ' +self.course)
       

lstObj=[]
for i in range(2):
    s=input()
    n=int(input())
    temp='obj'+str(i)
    temp=Student(s,n)

    lstObj.append(temp)
for i in lstObj:
    i.displayStudent()
