"""
my_module 
Author:25423
Date:2023/6/26
"""
def print_lines():
    print('-'*10)
# 实现'一切皆模块'
if __name__ == '__main__':
    name='lee' # 这个是测试数据 导入该模块时,别人不会看见,只有本文件运行能看到
    print(name)
