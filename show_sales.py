with open('bakery.csv', 'r', encoding='utf-8') as f:
    params = input()
    list = []
    for line in f:
        list.append(line)
    if len(params) == 1 and params.isdigit():
        start = int(params[0])
        for start in range(start-1, len(list), 1):
            print(list[start])
    elif len(params) == 3 and params[0].isdigit() and params[2].isdigit():
        start = int(params[0])
        end = int(params[2])
        for start in range(start -1, end, 1):
            print(list[start])
    elif len(params) == 0:
        start = 1
        for start in range(start - 1, len(list), 1):
            print(list[start])
    else:
        print('Введены некорректно параметры')
    f.close
