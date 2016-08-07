def p_decorate(func):
    def func_wrapper(name):
        return "<p>{}</p>".format(func(name))
    return func_wrapper


@p_decorate
def get_text(name):
    return "lorem ipsum, {} dolor sit amet".format(name)

print(get_text("John"))
