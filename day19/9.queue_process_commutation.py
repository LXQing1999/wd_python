"""
9.queue_process_commutation
Author:LXQing
Date:2023/08/29
"""
from multiprocessing import Process, Queue
import time


def write(q):
    for i in ['A', 'B', 'C']:
        print('Put %s to queue' % i)
        q.put(i)
        time.sleep(0.2)


def reader(q:Queue):
    while True:
        if not q.empty():
            value=q.get()
            print('Get %s from Queue.'%value)
            time.sleep(0.2)
        else:
            break



if __name__ == '__main__':
    q = Queue(10)  # 新建一个大小为10的队列
    # 传参的时候，要求args一定是元组，python内置一个解包操作，所以后面不加,逗号  会报错
    pw = Process(target=write, args=(q,))
    pr = Process(target=reader, args=(q,))
    pw.start()
    pr.start()
    pw.join()  # 回收
    pr.join()
