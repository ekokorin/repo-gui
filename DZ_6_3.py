def parc(str):
    list_1 = []
    i = 0
    while i < len(str):
        end_ind = str.find('\n')
        if end_ind == -1:
            end_ind = len(str)
        list_1.append(str[i:end_ind])
        if str.find('\n') != -1:
            str = str[str.find('\n') + 1:]
        else:
            str = ''
    return list_1


file_1 = open('users.csv', 'r', encoding='utf-8')
file_2 = open('hobby.csv', 'r', encoding='utf-8')
res = {}
content1 = file_1.read()
content2 = file_2.read()


def create_file(a, b):
    if len(parc(a)) < len(parc(b)):
        return print('Error code: 1')
    with open('result.csv', 'w', encoding='utf-8') as f:
        if len(parc(a)) == len(parc(b)):
            for i in range(len(parc(a))):
                res[parc(a)[i]] = parc(b)[i]
            f.write(str(res))
        else:
            for i in range(len(parc(b))):
                res[parc(a)[i]] = parc(b)[i]
            y = len(parc(b))
            while y < len(parc(a)):
                res[parc(a)[y]] = None
                y += 1
            f.write(str(res))


create_file(content1, content2)
file_1.close()
file_2.close()
