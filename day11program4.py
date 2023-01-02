#convert two list into dictionary
keys=['Ten','Twenty','Thirsty']
values=[10,20,30]
d=dict()
for i,j in zip(keys,values):
    d[i]=j

print(d)
