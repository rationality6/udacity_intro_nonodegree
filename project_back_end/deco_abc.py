def p_decorater(func):
    def wrapper(middle):
        print("a")
        print(func(middle))
        print("c")
    return wrapper


@p_decorater
def print_abc(middle):
    return middle

print_abc('b')
