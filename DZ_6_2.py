def parce(srting):
    ip = ''
    ip_end = ' - -'
    for i in range(len(srting)):
        ip = f'{srting[i:srting.find(ip_end, i, len(srting))]}'
        break
    return ip


list_ip = {}
file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')

for line in file_1:
    if parce(line) in list_ip.keys():
        list_ip[parce(line)] += 1
    else:
        list_ip[parce(line)] = 1
file_1.close()

for key, val in list_ip.items():
    if max(list(list_ip.values())) == val:
        print(f'IP спамер: {key}, сделал {val} запросов')

