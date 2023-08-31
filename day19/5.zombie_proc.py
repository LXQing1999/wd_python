"""
5.zombie_proc
经linux命令ps -elf后,python将进程名改为[python3.8] <defunct>
Author:LXQing
Date:2023/08/27
"""

import os
from multiprocessing import Process
import time
def run_proc():
    print('子进程：PID={}'.format(os.getpid()))
    print('子进程结束')

if __name__ == '__main__':
    # 注意传参的时候，目标函数不要加括号
    child_process=Process(target=run_proc)
    child_process.start()
    print('父进程：PID={}'.format(os.getpid()))
    print('每次都是优先调用main里的函数，再调用Process中的函数')
    while True:
        print('1')
        time.sleep(1)





















