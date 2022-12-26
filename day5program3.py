def extract_vowel(s):
    temp_vowel=''
    for i in s:
        #print("i:",i)
        if i in 'AEIOUaeiou':
            temp_vowel+=i
    return temp_vowel
#str1=input("enter the string:")
str1=input()
a=extract_vowel(str1)
print("vowels:",a)


##str1=input()
##temp_vowel=''
##for i in str1:
##    if i in 'AEIOUaeiou':
##        temp_vowel+=i
##print("vowels:",temp_vowel)
