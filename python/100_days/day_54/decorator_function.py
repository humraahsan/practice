import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    k = 1
    for i in range(100000):
        k = i * 1
    return k


@speed_calc_decorator
def slow_function():
    k = 1
    for i in range(100):
        k = i * i
    return k


if __name__ == '__main__':
    fast_function()
    slow_function()