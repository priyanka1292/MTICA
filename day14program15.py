class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("total  employee :" .format(Employee.empCount))
    def displayEmployee(self):
        print("Name: ",self.name, ",Salary: ",self.salary)
emp1=Employee("mahima",55000)
emp1.displayEmployee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))#return value of 'salary' attribute
setattr(emp1,'salary',7000)#set attribute 'salary' at 7000
print("modify salary:",getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','manager')
print(hasattr(emp1,'desg'))
print("added attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')#delete attribute 'salary' 
print("is salary an attribute:",hasattr(emp1,'salary'))


##getattr(object,attribute)
##setattr(object,attribute,value)
##hasattr(object,attribute)
##delattr(object,attribute)
