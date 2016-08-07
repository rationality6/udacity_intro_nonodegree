import datetime


def elapse_decorate(func):
    def wrapper(xrange, yrange, n):
        result_time_list = []
        for i in range(0, n):
            start_time = datetime.datetime.now()
            func(xrange, yrange, n)
            end_time = datetime.datetime.now()
            result_time = end_time - start_time
            result_time_list.append(str(result_time))
        return result_time_list
    return wrapper


@elapse_decorate
def foo(xrange, yrange, n):
    for x in range(xrange):
        for y in range(yrange):
            if x == (xrange - 1) and y == (yrange - 1):
                break

if __name__ == "__main__":
    print(foo(10000, 10000, 4))
