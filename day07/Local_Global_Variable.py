"""
LocalGlobal_variable
num在这里是形式参数 局部变量
Author:25423
Date:2023/6/26
"""

num = 10
def demo1():
    num = 20
    print('重新赋值后%d'%num)


def demo2():
    global num
    num+=2
    print('特意标明了是全局变量%d'%num)


demo1()
demo2()
print('全局变量已经被修改%d'%num)
print("end")
