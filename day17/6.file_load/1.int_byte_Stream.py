"""
1.int_byte_Stream
Author:LXQing
Date:2023/08/20
"""
import struct
import os
import time

train_content = '随便写点'.encode('utf8')
train_head = len(train_content)
print(train_head)
print(type(train_head))
print('-' * 20)

train_head_bytes = struct.pack('I', train_head)
print(train_head_bytes)
b=struct.unpack('I',train_head_bytes)
print(b[0])
print('-' * 20)
c=train_head_bytes+train_head_bytes
print(c)
