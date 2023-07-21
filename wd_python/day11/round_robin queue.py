"""
collections
注意一下文件的命名,避免重复引用
Author:LXQing
Date:2023/7/4
"""
from collections import deque
#增删查改
queue = deque(["Eric","John""Michaet"])
queue.append('luke')
print(queue)
print(queue.popleft())
print(queue)

queue[0] ='xiongda'
print(queue[0])
