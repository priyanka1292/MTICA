class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("total  employee :",Employee.empCount)
    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)
emp1=Employee("mahima",55000)
print("total employee",Employee.empCount)
emp2=Employee("Abhinn",54000)
emp1.displayEmployee()
emp2.displayEmployee()
print("total employee{0}" .format(Employee.empCount))
emp3=Employee("manu gupta",55500)
emp3.displayCount()
emp2.displayCount()
emp1.displayCount()
print("total employee{0}" .format(Employee.empCount))
    
