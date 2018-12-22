#decorators
#A decorator takes in a function, adds some functionality and returns it.

def cough_dec(func):

    def func_wrapper():

        print("************")
        func()
        print("------------")

    return func_wrapper

@cough_dec
def Hello():
    print("Hello")

@cough_dec
def Hi():
    print("Hi")

Hello()
Hi()
