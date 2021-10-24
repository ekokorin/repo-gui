my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
ind = 0
new_list = []
a = ''
prom_result = ''
result = ''
while ind < len(my_list):    #  Добавляем кавычки и 0
    if my_list[ind].isdigit():  #  Если элемент списка число
        if len(my_list[ind]) == 1:
            a = '0' + my_list[ind]
            new_list.append('"')
            new_list.append(a)
            new_list.append('"')
            a = ''
        else:
            new_list.append('"')
            new_list.append(my_list[ind])
            new_list.append('"')
    else:   # Тут проверяем строку на наличие цифр для числа со знаком +
        num = my_list[ind]
        for c in num:
            if c.isdigit():
                num = num[0] + '0' + c
                new_list.append('"')
                new_list.append(num)
                new_list.append('"')
        if not(my_list[ind].isdigit()) and my_list[ind].isalpha():
            new_list.append(my_list[ind])
    ind += 1
prom_result = ' '.join(new_list)  # склеиваем список в строку через пробелы
print(prom_result)


