src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]


def func_max(s):
    result = []
    for i in range(1, len(s)):
        if s[i] > s[i - 1]:
            result.append(s[i])
    yield result


print(list(func_max(src)))

