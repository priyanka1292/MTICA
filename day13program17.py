#add a new condition and use the raise keyword to raise an exception
#which is already handled

#a=-3
a=3
b=2
try:
    #condition for checking for negative values
    if a<0  or b<0:
        #raising an error using raising keyword
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("please enter valid integer value")
