"""
10.program_pool进程池
输出结果可以看到进程调用的顺序
Author:LXQing
Date:2023/08/29
"""
from multiprocessing.pool import Pool
import os, time, random


# 用于标识每个子进程执行的任务。
def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


if __name__ == '__main__':
    pool = Pool(3)
    for i in range(10):
        # 每次循环将会用空闲的子进程取调用目标
        # pool.apply_async 异步，用于向进程池中提交任务。第一个参数是要执行的函数，第二个参数是要传递给函数的参数。会立即返回一个结果对象，不会等待任务执行完成。
        pool.apply_async(worker, (i,))
    print('start')
    pool.close()  # 关闭进程池，表示不会再添加新的任务
    pool.join()  # 等待所有任务完成并回收子进程
    print('end')
