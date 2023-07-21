"""
dir_op 目录操作
Author:LXQing
Date:2023/7/3
"""
import os
def user_rename():
    os.rename('file','file1')
def user_remove():
    os.remove('file1')

# 以列表的形式返回
def user_listdir():
    print(os.listdir('.'))

# 递归调用,实现深度优先遍历
def dir_dsf(path):
    file_list=os.listdir(path)
    for filename in file_list:
        print(filename)
        if os.path.isdir(path+'/'+filename):
            dir_dsf(filename)
'''def list_dir(path):
    print(os.listdir())'''

if __name__ == '__main__':
    # user_rename()
    # user_remove()
    # user_listdir()
    dir_dsf('.')
    # os.listdir('dir_dfs')
