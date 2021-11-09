import os

import shutil

example_dir = 'my_project'
dst = 'my_project\\templates'
list_1 = list(os.walk(example_dir))

for i in list_1:
    print(i)
    if i[0].find('\\authapp\\templates') != -1 or i[0].find('mainapp\\templates') != -1:
        shutil.copytree(i[0], dst, dirs_exist_ok=True)



