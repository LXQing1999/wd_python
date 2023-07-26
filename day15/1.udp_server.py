"""
1.udp_server服务端
Author:LXQing
Date:2023/07/26
"""
import socket
# AF_INET用于Internet进程间通信
# 创建tcp套接字
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 写1024以上端口
# 这个私有地址 route -n
addr=('192.168.31.67',2000)
# 失败时抛出异常
s.bind(addr)
# receve要比发送的更高一些
# temp=s.recvfrom(5)
# print('utf8未解码：',temp[0])
# print('utf8解码适配多种语言：',temp[0].decode('utf8'))
# print('私有地址，接收数据：',temp[1])
data,client_addr=s.recvfrom(5)
print(data.decode('utf8'))
print(client_addr)
s.sendto('lana del rey'.encode('utf8'),client_addr)
s.close()

