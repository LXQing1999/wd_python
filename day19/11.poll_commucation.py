"""
11.poll_commucation 进程通信
Author:LXQing
Date:2023/08/29
"""
from multiprocessing import Pool, Manager
import os, time, random


def reader(q):
    print("reader启动（%s）,父进程为（%s）" % (os.getpid(), os.getpid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))


def writer(q):
    print("write启动（%s）,父进程（%s）" % (os.getpid(), os.getpid()))
    for i in "wangdao":
        q.put(i)


if __name__ == '__main__':
    q=Manager().Queue()
    print(q)
    po=Pool()  # 初始化进程池
    # async/await模式是一种存在于许多编程语言中的语法特性。这种模式使得异步非阻塞函数逻辑可以用一种类似于同步函数的方式进行构造。
    po.apply_async(writer,args=(q,))
    print(q)
    time.sleep(1)
    po.apply_async(reader,args=(q,))
    po.close()
    po.join()
