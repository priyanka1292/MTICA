def extractDigit(s):
    temp_digit=''
    for i in s:
        #print("i:",i)
        if i in '0123456789':
            temp_digit+=i
    return temp_digit
#str1=input("enter the string:")
str1=input()
a=extractDigit(str1)
print("digit",a)
