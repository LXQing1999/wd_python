"""
4.get_pid
终端命令 ps -elf|grep 4.get_pid.py 确实可以看到有两个进程编号
Author:LXQing
Date:2023/08/27
"""
import os
from multiprocessing import Process
import time
def run_proc():
    print('子进程：PID={}'.format(os.getpid()))
    # while True:
    #     time.sleep(1)
    print('子进程结束')

if __name__ == '__main__':
    # 注意传参的时候，目标函数不要加括号
    child_process=Process(target=run_proc)
    child_process.start()
    print('父进程：PID={}'.format(os.getpid()))
    print('每次都是优先调用main里的函数，再调用Process中的函数')



