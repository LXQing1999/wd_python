"""
if 
Author:25423
Date:2023/6/25
"""
def judge1():
    age=int(input('年龄:'))
    if age>=18:
        print('成年')
    else:
        print('未成年')
def judge2():
    aScore=60
    bScore=70
    if aScore >=60 and bScore >=60:
        print('pass')
    else:
        print('fail')
if __name__ == '__main__':
    judge1()
    judge2()