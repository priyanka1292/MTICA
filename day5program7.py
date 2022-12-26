def extract_consonant(s):
    temp_consonant=''
    for i in s:
        #print("i:",i)
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstuvwxyz':
            temp_consonant+=i
    return temp_consonant
#str1=input("enter the string:")
str1=input()
a=extract_consonant(str1)
print("consonant:",a)
