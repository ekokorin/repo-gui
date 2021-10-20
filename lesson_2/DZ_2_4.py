count = 10 # (10 элементов списка)
check = [5.58, 80, 200.56, 1121.66, 12.7, 2.2, 120.98, 4.44, 654.5, 15.04]
i = 0
print(check)
print('')
strin = ''
result = ''
while i < count:
    a = check[i] * 100
    r = int(a // 100)
    kk = int(a % 100)
    zero = ''
    if a % 100 < 10:
        zero = '0'
    strin = f'{r} руб {zero}{kk} коп'
    i += 1
    if result == '':
        result = strin
    else:
        result = f'{result}, {strin}'
print('Вывод на экран цен через запятую в одну строку в виде <r> руб <kk> коп:')
print(result)
print('')
sortcheck = check
sortcheck.sort() # Сортируем по возрастанию
print('Вывод цен отсортированных по возрастанию:')
i = 0
while i < count:
    print(sortcheck[i])
    i += 1
rev_check = sortcheck
rev_check.reverse()
i = 4
print('')
print('Вывод цен 5-ти самых дорогих товаров:')
while i >= 0:
    print(rev_check[i])
    i -= 1
