##def printDetails(marks=40,age=18,name):
def printDetails(name,marks=40,age=18):
    print("Name:",name)
    print("Marks:",marks)
    print("Age:",age)
    return None
##printDetails()#TYPE ERROR
##printDetails('Manohar')#TYPE error
##printDetails('Manohar',57)
##printDetails(67,'Manohar')
printDetails(marks=77,name='manohar')#keyword argument
