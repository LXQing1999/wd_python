"""
1.tcp_server服务器
真正的即时聊天
Author:LXQing
Date:2023/08/11
"""
import socket
import select
import sys


# 定义tcp服务器
def tcp_server():
    '''
    socket 是 Python 中的一个模块，提供了用于网络编程的功能。         socket.AF_INET 是一个常量，表示使用IPv4协议。
    socket.SOCK_STREAM 也是一个常量，表示使用TCP协议。
    socket.socket(socket.AF_INET, socket.SOCK_STREAM) 是一个函数调用，创建了一个套接字对象，该对象使用了IPv4协议和TCP协议。
    这个套接字对象可以用于建立客户端或服务器端的网络连接，通过调用套接字对象的方法，可以进行网络数据的发送和接收操作。'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.31.67', 2000)
    # 绑定,端口并没有激活
    s.bind(addr)
    # listen时，端口才激活
    s.listen(128)
    print('连接和监听的过程对程序员来说是透明的')
    new_client, client_addr = s.accept()
    print(client_addr)
    # 创建一个epoll对象
    # fileno文件描述符
    # select.EPOLLIN 可读事件
    epoll = select.epoll()
    # 让epoll监控new_client sys.stdin
    epoll.register(new_client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    print('fileno()用来取得参数stream指定的文件流所使用的文件描述词',new_client.fileno())
    client_list=[] # 存储所有的client对象
    # epoll.register()
    print(sys.stdin.fileno())
# fds数组就是需要监听的文件描述符数组
    while True:
        # 谁的缓冲区有数据，就填写到events
        events = epoll.poll(-1)
        for fd,event in events:
            #  recv、select和epoll都是阻塞方法   如果接收缓冲区有数据
            if fd == new_client.fileno():

                data = new_client.recv(100)
                print(data.decode('utf8'))
                if data:
                    print(data.decode('utf8'))
                else:
                    print('对方断开')
                    return
            elif fd == sys.stdin.fileno():
                try:
                    # 服务器端先接
                    data = input()  # 服务器端说话，发给用户端
                except EOFError:   # 按服务器后让
                    print('exit')
                    return
                new_client.send(data.encode('utf8'))
    new_client.close()  # 按Ctrl d客户端断开连接
    s.close()  # 关闭监听


if __name__ == '__main__':
    tcp_server()
