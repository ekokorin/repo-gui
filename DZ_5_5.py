src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
""" Определить элементы списка, не имеющие повторений"""

uniq_el = set()
tmp = set()
for el in src:
    if el not in tmp:
        uniq_el.add(el)
    else:
        uniq_el.discard(el)
    tmp.add(el)
result = [el for el in src if el in uniq_el]
print(result)
