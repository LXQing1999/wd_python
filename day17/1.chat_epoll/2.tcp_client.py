"""
2.tcp_client客户端
现在写的这个是只能发送一条消息的

netstat命令用于显示网络连接、路由表和网络接口信息等   netstat -an|grep 端口号
Author:LXQing
Date:2023/08/11
"""
import socket
import select
import sys

def tcp_client():
    if len(sys.argv)==1:
        return

    # ip地址和字节流
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destation_addr = (sys.argv[1], 2000)
    # tcp连接三次握手
    client.connect(destation_addr)

    epoll = select.epoll()
    # 让epoll监控new_client sys.stdin
    epoll.register(client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    print(client.fileno())
    # epoll.register()
    print(sys.stdin.fileno())

    while True:
        # 谁的缓冲区有数据，就填写到events
        # events是列表，里面存了元组（fd,event）
        events = epoll.poll(-1)
        for fd,event in events:
            # 如果接收缓冲区有数据
            if fd == client.fileno():
                data = client.recv(100)
                print(data.decode('utf8'))
            elif fd == sys.stdin.fileno():
                # 服务器端先接
                data = input()  # 服务器端说话，发给用户端
                client.send(data.encode('utf8'))
    client.close()

if __name__ == '__main__':

    tcp_client()
