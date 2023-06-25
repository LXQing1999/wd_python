"""
module 
Author:25423
Date:2023/6/26
"""
import module

def draw1():
    print('-'*8)
    print('draw1')
    print('-' * 8)
def draw2():
    print('-' * 8)
    print('draw2')
    draw1()
if __name__ == '__main__':
    module.draw2()
    print('time')