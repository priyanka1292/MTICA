def outer():
    print('outer function')
    def inner():
        print('inner fuction')
    inner()
outer()
