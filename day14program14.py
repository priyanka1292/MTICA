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
emp1.salary=67000 #modify 'salary' attribute
emp1.experience=3 #add an 'experience' attribute
emp1.displayEmployee()
emp1.name='Manoj' #modify 'name' attribute
emp1.displayEmployee()
print(emp1.experience)
#del emp1.salary #delete 'salary' attribute
emp1.displayEmployee()
