"""
7.shared_param父进程与子进程共享变量
Author:LXQing
Date:2023/08/27
"""
import os
from multiprocessing import Process
import time

nums = [11, 22]


def work1():
    print('work1的PID,{}'.format(os.getpid()))
    nums.append(33)
    time.sleep(0.2)
    print('work1元素', nums)


def work2():
    print('work2的PID,{}'.format(os.getpid()))
    print('work2元素', nums)

# 子进程是父进程创建的复制品，进程的资源是独立的
# 子进程变量
if __name__ == '__main__':
    p = Process(target=work1)
    p.start()
    p.join()
    p = Process(target=work2)
    p.start()
    p.join()
