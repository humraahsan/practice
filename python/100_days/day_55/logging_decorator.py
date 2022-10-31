def logging_decorator(function):
    def wrapper(*args):
        print(f"got function: {function.__name__}, and args: {args}")
        #print("got args: ", args)
        return function(*args)

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


print(a_function(1, 2, 3))
