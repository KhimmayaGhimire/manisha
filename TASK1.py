# import os,shutil
# os.mkdir('file')
# shutil.copytree('file','movies/file2')
# shutil.rmtree('movies/file2')
# shutil.move('file','movies/file')
# shutil.copy('read_file.py','movies/read_file.py')

import os
# os.mkdir(r'd:/manisha')
# open('list.txt','a')
# print(os.listdir())
# print(os.getcwd())

for item in os.listdir():
    # path=os.path.join(os.getcwd(),item)
    path=os.path.join(r'D:/',item)
    print(path)