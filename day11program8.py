##sample_dict={
##    "name": "kelly",
##    "age": 25,
##    "salary":8000,
##    "city":"New York"}
##keys=["name","salary"]

 
##newDict={}
##for i in keys:
##    newDict[i]=sample_dict[i]
##print(newDict)


##newDict={i:sample_dict[i] for i in keys }
##print(newDict)


sample_dict={
    "name": "kelly",
    "age": 25,
    "salary":8000,
    "city":"New York"}
#keys to extract
keys=["name","salary"]


#new dict
res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
