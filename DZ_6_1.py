
def parce(srting):
    remote_addr = ''
    request_type = ''
    requested_resource = ''
    ip_end = ' - -'
    req_start = '] "'
    req_type_end = ' /'
    req_res_end = ' HTTP'
    for i in range(len(srting)):
        remote_addr = f'{srting[i:srting.find(ip_end, i, len(srting))]}'
        request_type = f'{srting[(srting.find(req_start, i, len(srting))) + 3:srting.find(req_type_end, i, len(srting))]}'
        requested_resource = f'{srting[(srting.find(req_type_end, i, len(srting))) + 1:srting.find(req_res_end, i, len(srting))]}'
        break
    return remote_addr, request_type, requested_resource


result = []
file = open('nginx_logs.txt', 'r', encoding='utf-8')

for line in file:
        result.append(parce(line))
file.close()

print(result)
