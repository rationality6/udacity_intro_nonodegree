def decorate(func):
    def func_wrapper():
        print("welcome to")
        func()
        print("with python")
    return func_wrapper

@decorate
def function():
    print("hello world")

function()
