def val_checker(func):
    def wrapper(x):
        msg = f'wrong val: {x}'
        if x < 0:
            raise ValueError(msg)
        else:
            return func(x)

    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


#  print(calc_cube(3))
print(calc_cube(-5))
