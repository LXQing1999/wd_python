"""
elif 
Author:25423
Date:2023/6/25
"""


def compare(x):
    if x > 5:
        print('a')
    elif 3 < x < 5:
        print('b')
    elif 1 < x < 3:
        print('c')
    else:
        print('d')


if __name__ == '__main__':
    x = int(input('请输入:'))
    compare(x)
