def findFrequency(s):
    frequencyDict=dict() #creating empty dictionary
    for i in s:
        if i in frequencyDict:
            frequencyDict[i]+=1
        else:
            frequencyDict[i]=1
    return  frequencyDict

def formatOutput(d):
    for i in sorted(d):
        print(i,d[i])
        


n=int(input())
for i in range(n):
    inpStr=input()
    formatOutput(findFrequency(inpStr))
    
