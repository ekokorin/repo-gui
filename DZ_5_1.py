from itertools import islice
"""Генерирует список нечетных чисел"""

def count(n):
    for num in range(1, n + 1, 2):
        yield num


print(*islice(count(10), 15))
print(type(count(10)))
