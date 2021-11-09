import os

f_1 = open('config.yaml', 'r', encoding='utf-8')
flag_end = 0
for line in f_1:
    flag_start = int((line.find('|--') + 3) / 3)
    i = line.find('|--') + 3
    if flag_start < flag_end:
        for flag_start in range(flag_start, flag_end):
            os.chdir("..")
    if not os.path.exists(line[i:len(line) - 1]) and line.find('.') == -1:
        os.mkdir(line[i:len(line) - 1])
        dir_now = line[i:len(line) - 1]
        os.chdir(dir_now)
    if line.find('.') != -1:
        file_1 = open(line[line.find('|--') + 3:len(line) - 1], 'x', encoding='utf-8')
        file_1.close()
    flag_end = int((line.find('|--') + 3) / 3)
f_1.close()

