"""
12.loop_send_recv
Author:LXQing
Date:2023/08/31
"""
def cycle_recv(client,file,file_size):
    total=0
    while total<file_size:
        data=client.recv(1000)
        file.write(data)
        total+=len(data)
