"""
variable_adv 
Author:25423
Date:2023/6/26
"""


# int  4B =24b
# id显示该元素的地址
def var_id():
    a = 1
    print(id(a))
    print('将一个变量a赋给另一个变量b')
    b = a
    print(id(b))
    a = 2
    print('重新赋值')
    print(id(a))


# 数值改变后,对应的地址也发生了变化
def change(x):
    print(id(x))
    x += 1
    print('改变值')
    print(id(x))


def big_int_id():
    a = 10000000
    print(id(a))
    b = 10000000
    print(id(b))


if __name__ == '__main__':
    var_id()
    a = 10
    # 传递值,地址不发生改变
    print('传递值')
    print(id(a))
    change(a)
    print('大数')
    # 有时特别大的数字,会出现不同的地址
    big_int_id()
