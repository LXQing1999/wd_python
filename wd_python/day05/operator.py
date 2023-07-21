"""
operator 
Author:25423
Date:2023/6/25
"""


def function():
    # 默认是浮点数运算 保留小数
    print(5 / 2)
    # 整除
    print(5 // 2)
    # 余数
    print(5 % 2)
    print(2 * 3)
    # 幂函数
    print(2 ** 3)
    print(3 + 5 - 2)


# 关系运算和逻辑运算
def leap_year():
    year = int(input('请输入年份:'))
    print(year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


def logic():
    print('-' * 9)
    print(5 and 3)
    print(5 or 3)
    if -3:
        print('Here')
    print('-' * 9)


def compare():
    num = int(input('请输入某数:'))
    print(3 < num < 5)


if __name__ == '__main__':
    function()
    leap_year()
    compare()
    logic()
