employees=['kelly','Emma','Mansa']
defaults={"designation": 'Developer' , " salary": 80000}

data=dict.fromkeys(employees, defaults)
##for i in employees:
##    data[i]=defaults
print(data)


#individual data
print(data["Mansa"])
