from functools import wraps


def type_func(func):
    @wraps(func)
    def wrapper(*a, **ab):
        for i in a:
            s = {func(i): type(i)}
            print(s)
        for i in ab.values():
            s = {func(i): type(i)}
            print(s)
    return wrapper


@type_func
def calc_cube(x):
    return x ** 3


print(calc_cube(8))
print(calc_cube(5, 6, 10.5, 0.5))
print(calc_cube(a=10.6, b=9, c=1.5))
