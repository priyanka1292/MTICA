def extract_spchar(s):
    spchar=''
    temp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in s:
        #print("i:",i)
        if i not in temp:
            spchar+=i
    return spchar
#str1=input("enter the string:")
str1=input()
a=extract_spchar(str1)
print("special character:",a)
