def count_consonant(s):
    n_consonant=0
    for i in s:
        if i  in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstuvwxyz':
            n_consonant+=1
    return n_consonant
str1=input()
a=count_consonant(str1)
print("No of consonant in:'",str1,"'is",a)
