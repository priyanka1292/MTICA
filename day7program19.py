##def add_five(x):
##    temp=x+5
##    return temp
##nums=[11,22,33,44,55]
##result=list( map(add_five,nums))#map(function name,iterator)
##print(nums)
##print(result)
##print('-'*40)


nums=[11,22,33,44,55]
result=[i+5 for i in nums]
print(result)

