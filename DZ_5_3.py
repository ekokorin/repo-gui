tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Вася', 'Коля'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
if len(klasses) < len(tutors):
    i = 0
    while i < (len(tutors)-len(klasses)):
        klasses.append(None)

print(zip(tutors, klasses))

print(list(zip(tutors, klasses)))
