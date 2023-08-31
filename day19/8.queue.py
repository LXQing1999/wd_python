"""
8.queue
Author:LXQing
Date:2023/08/29
"""
from multiprocessing import Queue
# 初始化一个Queue对象，最多可接受三条put消息
q=Queue(3)
q.put(1)
q.put(2)
print('队列满了吗？',q.full())
q.put(3)
print('队列满了吗？',q.full())
# 队列已满后，再放就会报错
print(q.get())
print(q.get())
print(q.get())

# print(q.get())
