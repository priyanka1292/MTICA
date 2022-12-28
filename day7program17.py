#remove empty string
##lst=["Sedan","SUV","","","pickup",'','  ']
##ans=[]
##for i in lst:
##    if i:
##        ans.append(i)
##
##print(ans)

lst=["Sedan","SUV","","","pickup",'',"  "]
ans=[ i for i in lst  if i]
print(ans)
