"""
test.py
Author:LXQing
Date:2023/08/24
"""
import os
path=os.getcwd()
print(path)
# list_file=os.listdir(os.getcwd())
# 传入文件路径，返回文件大小和类型  state状态、
'''for i in list_file:
    print(type(os.stat(i)))
    print(os.stat(i).st_size)'''
data = ''
for file in os.listdir(path):
    # str(os.stat(file).st_size)将文件大小转换为字符串类型。    os.stat(file)查看文件状态
    data += file + ' ' * 5 + str(os.stat(file).st_size) + '\n'
print(data)

path='cd   dir1'.split()[1]
# os.chdir('H:\\')   # 改变当前工作目录。
print(os.getcwd())
os.remove('file123')


