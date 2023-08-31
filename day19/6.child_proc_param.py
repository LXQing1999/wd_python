"""
6.child_proc_param
结合C++知，**两个指针表示:可以传入接收任意数量的关键字参数，并将这些参数存储在一个字典中
Author:LXQing
Date:2023/08/27
"""
import os
from multiprocessing import Process
import time
def run_proc(name,age,**kwargs):
    for i in range(10):
        print('子进程{} {},{}'.format(name, age, kwargs))
        time.sleep(0.2)


if __name__ == '__main__':
    p=Process(target=run_proc,args=('lee',24),kwargs={'408':120})
    print('1')
    p.start()
    print('2')
    p.join(0)  # 一直等子进程，子进程结束就会回收pcb资源
    p.terminate()  # 给子进程发信号终止子进程
    print('3')
