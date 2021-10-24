from random import choice


def get_jokes(n, flag='yes'):

    """Возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    used_nouns = ['']
    used_adverbs = ['']
    used_adjectives = ['']
    a = ''
    b = ''
    c = ''
    i = 0
    result = []
    if flag == 'yes':  # если флаг = 'yes' (по умолчанию), то слова в шутках могут повторяться
        while i < n:
            result.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
            i += 1
        return print(result)
    else:  # во всех остальных случаях слова не должны повторяться и шуток получится всего 5,
        # если даже ошибочно ввели больше
        if n > 5:
            n = 5
        while i < n:
            while a in used_nouns:
                a = choice(nouns)
            while b in used_adverbs:
                b = choice(adverbs)
            while c in used_adjectives:
                c = choice(adjectives)
            result.append(f"{a} {b} {c}")
            used_nouns.append(a)
            used_adverbs.append(b)
            used_adjectives.append(c)
            i += 1
        return print(result)


get_jokes(4, 'no')
