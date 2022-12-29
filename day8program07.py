num1=input("Enter a number:")
num2=input("Enter a number:")

try:
    res=int(num1)/int(num2)
except (ZeroDivisionError,ValueError):
    print("Exception handled by manohar")
except ValueError:
    print("Exception handled by ganguly")
except Exception as ob:
    print(ob)
else:
    print(num1, '/' ,num2, '=', res)
finally:
    print("Thanks")

print("visit again at python class at MTICA")






##num1=input("Enter a number:")
##num2=input("Enter a number:")

##try:
##    res=int(num1)/int(num2)
#except ZeroDivisionError:
#    print("Exception handled by manohar")
##except (ZeroDivisionError,ValueError):
##    print("Exception handled by manohar")
#except ValueError:
#    print("Exception handled by manohar")
##except Exception as ob:
##    print(ob)
##else:
##    print(num1, '/' ,num2, '=', res)
##finally:
##    print("Thanks")
##
##print("visit again at python class at MTICA")

