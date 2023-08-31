"""
3.creat_process并发进程
Author:LXQing
Date:2023/08/27
"""
from multiprocessing import Process
import time


def run_process():
    while True:
        print('2' * 5)
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_process)
    p.start()
    while True:
        print('1' * 5)
        time.sleep(1)
