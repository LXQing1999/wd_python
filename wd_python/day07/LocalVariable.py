"""
LocalVariable
和c++不同的地方:for循环中定义的局部变量在循环结束后释放
在Python中,for循环中定义的变量在结束后仍然保留
Author:25423
Date:2023/6/26
"""


def local():
    for i in range(10):
        num = 12
    print(num)


if __name__ == '__main__':
    local()
