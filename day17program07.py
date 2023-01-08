import datetime
ob=datetime.datetime.now()
print(type(ob))
print("-",25)
print(ob)
print(ob.year)
print(ob.month)
print(ob.day)
print(ob.hour)
print(ob.minute)
print(ob.second)
str1=str(ob.hour)+':'+str(ob.minute)+':'+str(ob.second)
print(str1)
print("-"*25)
print("1 week ago it was:",ob-datetime.timedelta(weeks=1))
print("100 days ago it was:",ob-datetime.timedelta(days=100))
print("1 week from now it will be:",ob+datetime.timedelta(weeks=1))
print("1000 dayslater it was:",ob+datetime.timedelta(days=100))
bday_haritha=datetime.datetime(2002,11,14)
print("-"*25)
print("Birthday in....",ob-bday_haritha)
print("-"*25)



##<class 'datetime.datetime'>
##- 25
##2023-01-08 12:08:20.511238
##2023
##1
##8
##12
##8
##20
##12:8:20
##-------------------------
##1 week ago it was: 2023-01-01 12:08:20.511238
##100 days ago it was: 2022-09-30 12:08:20.511238
##1 week from now it will be: 2023-01-15 12:08:20.511238
##1000 dayslater it was: 2023-04-18 12:08:20.511238
##-------------------------
##Birthday in.... 7360 days, 12:08:20.511238

