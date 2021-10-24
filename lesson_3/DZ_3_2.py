def num_translate(a):
    """Переводит числительные от 0 до 10 c английского на русский язык"""

    my_dict = {'zero': 'ноль',
               'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}
    if a.istitle():
        a = a.lower()
        if a in my_dict.keys():
            print(my_dict[a].capitalize())
        else:
            print(None)
    else:
        if a in my_dict.keys():
            print(my_dict[a])
        else:
            print(None)


s = input('Введите число на английском языке с 0 до 10: ')
num_translate(s)
