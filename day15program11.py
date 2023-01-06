#first function
def f():
    x=10
    print('id(x) in f outer:',id(x))
    #nested function
    def g():
        nonlocal x
        x=15
        print('id(x) in g inner:',id(x))
    g()
    print(x)
f()
