import os

import shutil

example_dir = 'repo-gui'
my_stat = {10: 0,
           100: 0,
           1000: 0,
           10000: 0,
           100000: 0}


def statist(file, my_stat):
    for key in my_stat.keys():
        if os.stat(file).st_size > 100000:
            my_stat[100000] += 1
        elif os.stat(file).st_size > 10000:
            my_stat[10000] += 1
        elif os.stat(file).st_size > 1000:
            my_stat[1000] += 1
        elif os.stat(file).st_size > 100:
            my_stat[100] += 1
        elif os.stat(file).st_size > 10:
            my_stat[10] += 1


for (dirpath, dirnames, filenames) in os.walk(example_dir):
    statist(filenames, my_stat)
    break

print(my_stat)
